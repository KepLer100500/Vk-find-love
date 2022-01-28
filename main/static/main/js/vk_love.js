const App = {
    data() {
        return {
            selectedInterest: -1,
            interests: ['Попугаи', 'it'],
            new_interest: "",
        }
    },
    methods: {
        addInterest() {
            if (this.new_interest !== "") {
                this.interests.push(this.new_interest);
                this.new_interest = "";
            }
        },
        removeInterest() {
            if(this.selectedInterest >= 0) {
                this.interests.splice(this.selectedInterest, 1);
                this.selectedInterest = -1;
            }
        },
        start_search() {
            var csrftoken = $("[name=csrfmiddlewaretoken]").val();
            axios({
                method: 'post',
                url: '/test_api/',
                data: {
                    interests: this.interests,
                },
                headers: {
                    "X-CSRFToken": csrftoken
                },
            }).then(response => (
                console.log("")
            ));
            window.location.replace("/gotcha/");
        },
    },
}

Vue.createApp(App).mount('#app')
