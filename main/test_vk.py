# -*- coding: utf-8 -*-
from vk_api import VkApi
from multiprocessing.pool import ThreadPool
from .models import *


class Group:
    def __init__(self, id, name, interest, users):
        self.id = id
        self.name = name
        self.interest = interest
        self.users = users


class UserVk:
    def __init__(self, id, groups, first_name='', last_name='',
                 bdate='', city='', country='', photo_200=''):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.bdate = bdate
        self.city = city
        self.country = country
        self.photo_200 = photo_200
        self.groups = groups


def get_session():
    session = VkApi('vk_login', 'vk_pass')
    session.auth()
    return session.get_api()


def groups_search(session, user_input_interest, count_got_groups):
    groups = session.groups.search(q=user_input_interest, count=count_got_groups, sort=6, v=5.131)
    groups_can_access_members = [group for group in groups['items'] if check_open_group(session, group['id'])]
    return groups_can_access_members


def check_open_group(session, group_id):
    try:
        session.groups.getMembers(group_id=group_id, offset=0, count=1, v=5.131).keys()
        return True
    except:
        return False


def count_members(session, group_id):
    return session.groups.getMembers(group_id=group_id, offset=0, count=1, v=5.131)['count']


def get_members_in_group_with_offset(session, group_id, offset):
    members = set(session.groups.getMembers(group_id=group_id, offset=offset,
                                            count=1000, v=5.126, sort='id_desc')['items'])
    return members


def get_members(session, group_id):
    pool = ThreadPool(processes=1)
    # count_users_in_group = count_members(session, group_id) # get all members
    count_users_in_group = 10000  # get first 10000 members
    members = set()
    for offset in range(0, count_users_in_group + 1, 1000):
        async_result = pool.apply_async(get_members_in_group_with_offset, (session, group_id, offset))
        members |= async_result.get()
    return members


def user_page_is_open(session, user_id):
    user_status = session.users.get(user_ids=user_id, v=5.126)[0]
    if 'is_closed' in user_status.keys():
        if not user_status['is_closed']:
            return True
    return False


def update_user_details(session, user):
    user_details = session.users.get(user_ids=user.id, fields='bdate, '
                                                              'city, country, photo_200', v=5.126)[0]
    user.first_name = user_details.get('first_name', '')
    user.last_name = user_details.get('last_name', '')
    user.bdate = user_details.get('bdate', '')
    user.city = user_details.get('city', '')
    user.country = user_details.get('country', '')
    user.photo_200 = user_details.get('photo_200', '')


def main_search(interests, user_id):
    current_user = User.objects.get(pk=user_id)
    search = Search(user_searcher=current_user, in_work_now=True)
    search.save()

    session = get_session()
    count_got_groups = 2
    all_users_all_themes = []
    all_groups = []
    for interest in interests.get('interests'):
        all_users_one_theme = set()
        open_groups = groups_search(session, interest, count_got_groups)
        for group in open_groups:
            id_group = group['id']
            name_group = group['name']
            pool = ThreadPool(processes=1)
            async_result = pool.apply_async(get_members, (session, id_group))
            users = async_result.get()
            all_groups.append(Group(id_group, name_group, interest, users))
            print(f'In work - id{id_group}, {name_group}')
            all_users_one_theme.update(users)
        all_users_all_themes.append(all_users_one_theme)

    for repeated_user in set.intersection(*all_users_all_themes):
        if user_page_is_open(session, repeated_user):
            print(f'Find user -> {repeated_user}')
            user = UserVk(repeated_user, [])
            update_user_details(session, user)
            candidate = Candidate(vkid=repeated_user, search=search, first_name=user.first_name, last_name=user.last_name,
                                  bdate=user.bdate, city=user.city, country=user.country, photo_200=user.photo_200)
            candidate.save()
            for group in all_groups:
                if repeated_user in group.users:
                    candidate_groups = CandidateGroups(candidate=candidate, group_name=group.name)
                    candidate_groups.save()

    search_finish = Search.objects.get(pk=search.pk)
    search_finish.in_work_now = False
    search_finish.save()
