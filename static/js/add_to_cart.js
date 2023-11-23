$(document).ready(function() {
    const csrf = getCookie('csrftoken');

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

    function getCookie(name) {
          const value = `; ${document.cookie}`;
          const parts = value.split(`; ${name}=`);
          if (parts.length === 2) {
            const csrfToken = parts.pop().split(';').shift();
            return csrfToken;
          }
          return null;
        }
});