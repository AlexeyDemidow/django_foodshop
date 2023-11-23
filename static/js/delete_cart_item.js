window.addEventListener("load",function() {
    $(document).ready(function () {
        const csrf = getCookie('csrftoken');

        $('.delete-cart-item').on('click', function () {
            const productId = $(this).data('product-id');
            console.log('dsfSVsb')
            $.ajax({
                url: `/cart/delete_cart_item/${productId}/`,
                type: 'POST',
                dataType: 'json',
                data: {
                    'csrfmiddlewaretoken': csrf,
                },
                success: function () {
                    $('#cart-item-' + productId).remove()
                    elementUpdate('#cart')
                    console.log('Удалено')
                },
                error: function (error) {
                    console.error(error);
                }
            });
        });


        async function elementUpdate(selector) {
            try {
                let html = await (await fetch(location.href)).text();
                let newdoc = new DOMParser().parseFromString(html, 'text/html');
                document.querySelector(selector).outerHTML = newdoc.querySelector(selector).outerHTML;
                location.reload(); // Добавлено полное обновление страницы потому что после выполнения функции не работают скрипты
                console.log('Элемент ' + selector + ' был успешно обновлен');
                return true;
            } catch (err) {
                console.log('При обновлении элемента ' + selector + ' произошла ошибка:');
                console.dir(err);
                return false;
            }
        }

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
})