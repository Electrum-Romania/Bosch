document.querySelectorAll('.menu-button').forEach((b) => {
    b.addEventListener('click', () => {
        if(b.classList.contains('clicked')) {
            b.classList.remove('clicked')
        }
        else {
            b.classList.add('clicked');

            document.querySelectorAll('.menu-button').forEach((bt) => {
                if (b.id !== bt.id) {
                    bt.classList.remove('clicked');
                }
            });
        }
    });
});