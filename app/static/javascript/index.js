document.addEventListener("DOMContentLoaded", function(event) {
    document.querySelectorAll('.table-btn').forEach(button => {
        button.addEventListener('click', (e) => {
            e.preventDefault();
            console.log(e.target.id.split("_")[0])
            check_id = e.target.id.split("_")[0]
            action = e.target.id.split("_")[1]
            document.querySelectorAll(  `#${check_id}`).forEach(checkbox => {
                checkbox.checked = (action === 'all')
            })
        })
    })
});