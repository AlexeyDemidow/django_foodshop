$(document).ready(function() {
    const csrf = getCookie('csrftoken');

    $('.plus-quantity').on('click', function() {
        const productId = $(this).data('product-id');
        let quantity = parseInt($('#item-quantity-' + productId).html())

        let price = parseFloat($('#item-price-' + productId).html().toString().replace(',', '.'))
        let item_price_final = price + price / quantity

        let sum_price = parseFloat($('#final-price').html().toString().replace(',', '.'))
        console.log(sum_price)
        let final_sum_price = sum_price + price / quantity
        console.log(price / quantity)
        console.log(final_sum_price)
        $.ajax({
            url: `/cart/add_to_cart/${productId}/`,
            type: 'POST',
            dataType: 'json',
            data: {
                'csrfmiddlewaretoken': csrf,
            },
            success: function() {
                $('#item-quantity-' + productId).html(quantity + 1)
                $('#item-price-' + productId).html(item_price_final.toFixed(2).toString().replace('.', ','))
                $('#final-price').html(final_sum_price.toFixed(2).toString().replace('.', ','))
                },
            error: function(error) {
                console.error(error);
            }
        });
    });

    $('.minus-quantity').on('click', function() {
        const productId = $(this).data('product-id');
        let quantity = parseInt($('#item-quantity-' + productId).html()) - 1

        let price = parseFloat($('#item-price-' + productId).html().toString().replace(',', '.'))
        let item_price_final = price - (price / (quantity + 1))

        let sum_price = parseFloat($('#final-price').html().toString().replace(',', '.'))
        let final_sum_price = sum_price - (price / (quantity + 1))
        if (quantity < 1) {
            quantity = 1
            final_sum_price = sum_price
        }
        if (item_price_final < price - (price / (quantity + 1))) {
            item_price_final = parseFloat(price)
        }
        $.ajax({
            url: `/cart/minus_quantity/${productId}/`,
            type: 'POST',
            dataType: 'json',
            data: {
                'csrfmiddlewaretoken': csrf,
            },
            success: function() {
                $('#item-quantity-' + productId).html(quantity)
                $('#item-price-' + productId).html(item_price_final.toFixed(2).toString().replace('.', ','))
                $('#final-price').html(final_sum_price.toFixed(2).toString().replace('.', ','))
                },
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