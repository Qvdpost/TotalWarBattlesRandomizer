document.addEventListener("DOMContentLoaded", function(event) {

    // Listener event for All and None checkbox buttons
    document.querySelectorAll('.table-btn').forEach(button => {
        button.addEventListener('click', (button_event) => {
            // Prevents form submission
            button_event.preventDefault();

            // Check or uncheck all boxes
            flip_all_checkboxes(button_event);
        })
    })
});

function flip_all_checkboxes(button) {
    // Get the correct column of boxes to check and the selected action (All vs None)
    check_id = button.target.id.split("_")[0]
    action = button.target.id.split("_")[1]
    
    document.querySelectorAll(  `#${check_id}`).forEach(checkbox => {
        // Checks the box if the 'All' button was pressed, else the box is unchecked.
        checkbox.checked = (action === 'all')
    })
}