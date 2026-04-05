document.querySelectorAll(".navlist li").forEach(nav => {
    nav.addEventListener("click", (e) => {
        document.querySelectorAll(".navlist li").forEach(n => n.classList.remove("activeNav"));
        e.currentTarget.classList.add("activeNav");
        })
    });


document.getElementById("editProfileButton").addEventListener("click", () => {
    window.location.href = "/main/EditTradesperson";
});

document.getElementById("WorkNavControl_id").addEventListener("click", function() {
    const element = document.getElementById('WorkSideNav_id');
    const list = Array.from(element.classList);
    
    if (list.includes("navOpen")) {
        element.classList.remove("navOpen");
        element.classList.add("navClose"); 
    } else {
        element.classList.remove("navClose");
        element.classList.add("navOpen"); 
    }
});


const sections = document.querySelectorAll(".mainSections");

const observer = new IntersectionObserver((entries) => {
    let dateHeaderTime = '';
    entries.forEach((entry) => {
    if (entry.isIntersecting) {
      console.log(entry.target.id + " is in the viewport");
      const id = entry.target.id;
      
      document.querySelectorAll(".navlist li").forEach(nav => nav.classList.remove("activeNav"));
      document.querySelector(`a[href="#${id}"]`).parentElement.classList.add("activeNav");


      // Do anything you want here 👇
      entry.target.classList.add("activeSection");

      if (entry.target.classList.contains("Notifications_section")) {
        const notificationsContainer =document.querySelector('.notificationCats');
        notificationsContainer.innerHTML = "";
        if (notificationsContainer) {
            async function getNotifications() {
            
                try {
                    const response = await fetch('http://localhost:8000/api/v1/notifications/')
                    const data = await response.json()
                    return data;
                } catch (error) {
                    console.log(error)
                }
            }
            
            getNotifications().then(data => {
                if (data) {
                    data.forEach(notification => {
                        const today = new Date();
                        const notificationDate = new Date(notification.created_at);

                        function dateHeader() {
                            if ((notificationDate.getDate() === today.getDate()) && (notificationDate.getMonth() === today.getMonth()) && (notificationDate.getFullYear() === today.getFullYear())) {
                            const notificationTimeElement = document.createElement('div');
                            notificationTimeElement.classList.add('notificationDay');
                            notificationTimeElement.innerHTML = `<p>Today</p>`;
                            notificationsContainer.appendChild(notificationTimeElement);
                            } else {
                                const notificationTimeElement = document.createElement('div');
                                notificationTimeElement.classList.add('notificationDay');
                                notificationTimeElement.innerHTML = `<p>${notificationDate.toLocaleDateString()}</p>`;
                                notificationsContainer.appendChild(notificationTimeElement);
                            }
                            return notificationDate.toLocaleDateString();
                        }

                        

                        // Function to create a notification card
                        function createNotificationCard(title, time, details, is_read) {
                            // Outer card
                            const card = document.createElement("div");

                            if (is_read) {
                                card.classList.add("notificationCardOld");
                            }else {
                                card.classList.add("notificationCard");
                            }

                            // Switch div with SVG
                            const switchDiv = document.createElement("div");
                            switchDiv.classList.add("switch");
                            switchDiv.innerHTML = `
                                <svg width="8" height="8" viewBox="0 0 8 8" fill="none" xmlns="http://www.w3.org/2000/svg">
                                <circle cx="4" cy="4" r="4" />
                                </svg>
                            `;

                            // Title and time
                            const titleAndTime = document.createElement("div");
                            titleAndTime.classList.add("TitleAndTime");

                            const h3 = document.createElement("h3");
                            h3.textContent = title;

                            const timeEl = document.createElement("time");
                            timeEl.setAttribute("datetime", time);
                            timeEl.textContent = time;

                            titleAndTime.appendChild(h3);
                            titleAndTime.appendChild(timeEl);

                            // Details
                            const detailsDiv = document.createElement("div");
                            detailsDiv.classList.add("details");
                            detailsDiv.textContent = details;

                            // Assemble card
                            card.appendChild(switchDiv);
                            card.appendChild(titleAndTime);
                            card.appendChild(detailsDiv);

                            return card;
                        }
                        

                    if (dateHeaderTime === notificationDate.toLocaleDateString()) {
                        const notificationCard = createNotificationCard(notification.title, notificationDate.toLocaleTimeString(), notification.details, notification.is_read);
                        notificationsContainer.appendChild(notificationCard);
                    } else {
                        dateHeaderTime = dateHeader();
                        const notificationCard = createNotificationCard(notification.title, notificationDate.toLocaleTimeString(), notification.details, notification.is_read);
                        notificationsContainer.appendChild(notificationCard);
                    }

                });
                }
            });

        }
        
      }
    
    }
  });
}, {
  threshold: 0.6   // 60% of the section must be visible
});

sections.forEach(section => observer.observe(section));