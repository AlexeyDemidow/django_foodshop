window.addEventListener('load', function() {
    const searchInput = document.getElementById('search-input')
    const resultsBox = document.getElementById('result-box')
    const csrf = getCookie('csrftoken');

    const sendSearchData =(food) => {
        $.ajax({
            type: 'POST',
            url: 'food_search/',
            data: {
                'csrfmiddlewaretoken': csrf,
                'food': food
            },
            success: (res)=> {
                data = res.data
                if (Array.isArray(data)) {
                    resultsBox.innerHTML = ''
                    data.forEach(food=> {
                        resultsBox.innerHTML += `
                            <div class="catalog">
                                <div class="food_container">
                                    <a href="${food.id}/">
                                        <p><img src="${ food.pic }" style="width: 160px"></p>
                                        <p>${ food.name }</p>
                                        ${ food.price } BYN<br>
                                        ${ food.weight } г<br>                  
                                    </a>
                                    <button class="add-to-cart-btn" data-product-id="${ food.id }">Добавить в корзину</button>
                                </div>
                            </div>`
                    })
                    $('.add-to-cart-btn').on('click', function() {
                        const productId = $(this).data('product-id');
                        $.ajax({
                            url: `/cart/add_to_cart/${productId}/`,
                            type: 'POST',
                            dataType: 'json',
                            data: {
                                'csrfmiddlewaretoken': csrf
                            },
                            success: function(data) {
                                if (data.success === 'success') {
                                    $(this).text('В корзине').attr('disabled', true);
                                }
                            }.bind(this),
                            error: function(error) {
                                console.error(error);
                            }
                        });
                    });
                } else {
                    resultsBox.innerHTML = `<b>${data}</b>`
                }
            },
            error: (err)=> {
                console.log(err)
            }
        })
    }



    searchInput.addEventListener('keyup', e=>{
        sendSearchData(e.target.value)
    })

    function getCookie(name) {
          const value = `; ${document.cookie}`;
          const parts = value.split(`; ${name}=`);
          if (parts.length === 2) {
            const csrfToken = parts.pop().split(';').shift();
            return csrfToken;
          }
          return null;
        }
})


