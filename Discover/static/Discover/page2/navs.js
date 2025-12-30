if (document.location.pathname == '/main/Work') {
    active = document.getElementById('Work_id')
    active.classList.add('activeNav')
} else if (document.location.pathname == '/main/Profile') {
    active = document.getElementById('Profile_id')
    active.classList.add('activeNav')
} else if (document.location.pathname == '/main/Discover') {
    active = document.getElementById('Discover_id')
    active.classList.add('activeNav')
} else if (document.location.pathname == '/main/Notifications') {
    active = document.getElementById('Notifications_id')
    active.classList.add('activeNav')
} else if (document.location.pathname == '/main/More') {
    active = document.getElementById('More_id')
    active.classList.add('activeNav')
}