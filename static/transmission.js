



$(document).ready(function() {
        $('#sendButton').click(function(e) {
            console.log("click")
            function getCookie(name) {
                let cookieValue = null;
                if (document.cookie && document.cookie !== '') {
                    const cookies = document.cookie.split(';');
                    for (let i = 0; i < cookies.length; i++) {
                        const cookie = cookies[i].trim();
                        if (cookie.substring(0, name.length + 1) === (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
            return cookieValue;
            }
            e.preventDefault();
            var csrftoken = getCookie('csrftoken');
            const inputText = $('#inputText').val();
            console.log(inputText)
            $.ajax({
                type: 'POST',
                url: '/process/',
                headers: {
                'X-CSRFToken': csrftoken
                },
                data: JSON.stringify({
                'input_text': inputText  // set을 배열로 변환하여 전송
                }),
                success: function(response) {
                    let text = response["response_text"];
                    const outputElement = document.getElementById('dream-container');
                    outputElement.innerHTML = "";
                    let index = 0;

                    function typeText() {
                        if (index < text.length) {
                            outputElement.innerHTML += text.charAt(index);
                            console.log(text.charAt(index));
                            index++;
                            setTimeout(typeText, 30); // Adjust the delay (in milliseconds) as needed
                        }
                    }

                    typeText(); // Start typing text

                    // 성공 시 처리 로직
                },
                error: function(error) {
                    console.log(error);
                    // 오류 처리 로직
                }
            });
        });
    });
