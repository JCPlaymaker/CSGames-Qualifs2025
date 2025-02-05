# Solution
##### Pour ce défi, on n'avait qu'à regarder le code source pour voir que dans un script on voyait 
```js
<script>
        function locator_encoder() {
            const value = "L2hpZGRlbi9mbGFn";
            return atob(value);
        }
        function validate(e) {
            e.preventDefault();
            if (document.querySelector('input[name="username"]').value === 'admin' && document.querySelector('input[name="password"]').value === 'p3$$w0rD123') {
                window.location.href = locator_encoder();
            } else {
                const $error = document.getElementById('error-message');
                $error.classList.remove('hidden')
                const response = {
                    error: "Identifiants incorrects. Réessaie !"
                }
                $error.innerHTML = response.error;
            }
            return false;
        }
    </script>
```
##### La ligne qui nous intéresse est celle-ci
``if (document.querySelector('input[name="username"]').value === 'admin' && document.querySelector('input[name="password"]').value === 'p3$$w0rD123') {``
qui contient les credentials ``admin:p3$$w0rD123``\n
Flag: LEGO-4u7h3n71c4710n-101-028a4d
