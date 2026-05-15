 const switchBtnTradespeople = document.querySelector('.switchTradespeople');
 const switchJob = document.querySelector('.switchJob');

 if (switchBtnTradespeople) {
    switchBtnTradespeople.addEventListener('click', () => {
        const findTradespeople = document.querySelector('#containerHolder1');
        const findJobPostings = document.querySelector('#containerHolder2');
        findTradespeople.style.display = 'none';
        findJobPostings.style.display = 'block';
    });
 };
 if (switchJob) {
    switchJob.addEventListener('click', () => {
        const findTradespeople = document.querySelector('#containerHolder1');
        const findJobPostings = document.querySelector('#containerHolder2');
        findTradespeople.style.display = 'block';
        findJobPostings.style.display = 'none';
    });
 };

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

async function getData(apiUrl) {
    try {
        const response = await fetch(apiUrl)
        const data = await response.json()
        return data;
    } catch (error) {
        console.log(error)
    }

}

const observecontainerHolders = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                if (entry.target.id === "containerHolder1") {
                    alert("Tradespeople section is in view");

                    const tradespeopleCards = document.querySelector('.tradespeopleCards');
                    tradespeopleCards.innerHTML = "";

                    getData('http://localhost:8000/api/v1/tradespeople/').then(data => {

                        function createCard(tradesperson) {
                            const card = document.createElement('div');
                            card.classList.add('card');
                            card.dataset.tradespersonId = tradesperson.id;

                            const cardFisrtSection = document.createElement('div');
                            cardFisrtSection.classList.add('cardSections', 'cardDetails');
                            const profileIMG = document.createElement('div');
                            profileIMG.classList.add('profileIMG');
                            const profileImgEl = document.createElement('img');
                            profileImgEl.src = tradesperson.profile_picture;
                            profileImgEl.alt = 'profile image';
                            profileImgEl.width = 100;
                            profileImgEl.height = 100;
                            profileIMG.appendChild(profileImgEl);
                            const profileINFO = document.createElement('div');
                            profileINFO.classList.add('profileINFO');
                            const profileName = document.createElement('div');
                            profileName.classList.add('profileName');
                            profileName.innerHTML = `<h3>${tradesperson.first_name} ${tradesperson.last_name}</h3><svg xmlns="http://www.w3.org/2000/svg" id="verified" data-name="Layer 1" viewBox="0 0 24 24">
                                                                <path d="m23.126,9.868h0l-2.151-2.154v-1.718c0-1.651-1.342-2.995-2.991-2.995h-1.716l-2.151-2.153c-1.131-1.131-3.101-1.131-4.231,0l-2.151,2.153h-1.716c-1.65,0-2.991,1.343-2.991,2.995v1.718l-2.152,2.154c-1.165,1.168-1.165,3.067,0,4.235l2.151,2.154v1.718c0,1.651,1.342,2.995,2.991,2.995h1.716l2.151,2.153c.565.565,1.317.877,2.116.877s1.55-.312,2.115-.877l2.151-2.153h1.716c1.65,0,2.991-1.343,2.991-2.995v-1.718l2.152-2.154c1.165-1.168,1.165-3.067,0-4.235Zm-4.922.343l-5.054,4.995c-.614.61-1.423.916-2.231.916s-1.613-.305-2.229-.913l-2.599-2.499c-.392-.389-.396-1.021-.007-1.414.39-.391,1.021-.396,1.415-.007l2.598,2.498c.453.449,1.19.45,1.644,0l5.055-4.996c.394-.39,1.026-.386,1.415.007s.385,1.025-.007,1.414Z"></path>
                                                            </svg>`;
                            const profileTradeType = document.createElement('p');
                            profileTradeType.classList.add('profileTradeType');
                            profileTradeType.textContent = tradesperson.trade_category;
                            const profileTags = document.createElement('div');
                            profileTags.classList.add('profileTags');
                            
                            tradesperson.skills.forEach(specialty => {
                                const tag = document.createElement('p');
                                tag.classList.add('tags');
                                tag.textContent = specialty.name;
                                profileTags.appendChild(tag);
                            });

                            const profileLocation = document.createElement('p');
                            profileLocation.classList.add('profileLocation');
                            profileLocation.innerHTML = `<svg width="12" height="12" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">
                                                            <g clip-path="url(#clip0_125_77)">
                                                            <path d="M6 3C5.60444 3 5.21776 3.1173 4.88886 3.33706C4.55996 3.55682 4.30362 3.86918 4.15224 4.23463C4.00087 4.60009 3.96126 5.00222 4.03843 5.39018C4.1156 5.77814 4.30608 6.13451 4.58579 6.41421C4.86549 6.69392 5.22186 6.8844 5.60982 6.96157C5.99778 7.03874 6.39992 6.99914 6.76537 6.84776C7.13082 6.69638 7.44318 6.44004 7.66294 6.11114C7.8827 5.78224 8 5.39556 8 5C8 4.46957 7.78929 3.96086 7.41422 3.58579C7.03914 3.21071 6.53043 3 6 3ZM6 6C5.80222 6 5.60888 5.94135 5.44443 5.83147C5.27998 5.72159 5.15181 5.56541 5.07612 5.38268C5.00043 5.19996 4.98063 4.99889 5.01922 4.80491C5.0578 4.61093 5.15304 4.43275 5.29289 4.29289C5.43275 4.15304 5.61093 4.0578 5.80491 4.01921C5.99889 3.98063 6.19996 4.00043 6.38268 4.07612C6.56541 4.15181 6.72159 4.27998 6.83147 4.44443C6.94135 4.60888 7 4.80222 7 5C7 5.26522 6.89464 5.51957 6.70711 5.70711C6.51957 5.89464 6.26522 6 6 6Z" fill="#000080"></path>
                                                            <path d="M5.99991 12C5.57888 12.0022 5.16347 11.9034 4.78844 11.712C4.41342 11.5207 4.08971 11.2422 3.84441 10.9C1.93891 8.27152 0.972412 6.29552 0.972412 5.02652C0.972412 3.69315 1.50209 2.41438 2.44493 1.47154C3.38777 0.528705 4.66654 -0.000976562 5.99991 -0.000976562C7.33329 -0.000976562 8.61205 0.528705 9.55489 1.47154C10.4977 2.41438 11.0274 3.69315 11.0274 5.02652C11.0274 6.29552 10.0609 8.27152 8.15541 10.9C7.91011 11.2422 7.5864 11.5207 7.21138 11.712C6.83636 11.9034 6.42094 12.0022 5.99991 12ZM5.99991 1.09052C4.95612 1.09171 3.95542 1.50689 3.21735 2.24496C2.47928 2.98303 2.0641 3.98373 2.06291 5.02752C2.06291 6.03252 3.00941 7.89102 4.72741 10.2605C4.87326 10.4614 5.0646 10.6249 5.28577 10.7377C5.50694 10.8504 5.75166 10.9092 5.99991 10.9092C6.24816 10.9092 6.49288 10.8504 6.71406 10.7377C6.93523 10.6249 7.12656 10.4614 7.27241 10.2605C8.99041 7.89102 9.93691 6.03252 9.93691 5.02752C9.93572 3.98373 9.52055 2.98303 8.78248 2.24496C8.0444 1.50689 7.0437 1.09171 5.99991 1.09052Z" fill="#000080"></path>
                                                            </g>
                                                            <defs>
                                                            <clipPath id="clip0_125_77">
                                                            <rect width="12" height="12" fill="white"></rect>
                                                            </clipPath>
                                                            </defs>
                                                            </svg>${tradesperson.sub_location}`;
                            
                            const profileRate = document.createElement('p')
                            profileRate.classList.add('profileRate');
                            profileRate.innerHTML = `<svg width="12" height="12" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">
                                                            <g clip-path="url(#clip0_125_80)">
                                                            <path d="M11.5 9H9.4065C9.2855 9 9.1665 9.02 9.05 9.0485L6.443 6.7245L7.01 6.2015C7.148 6.0715 7.329 5.9995 7.5195 5.9995C7.6875 5.9995 8.1305 6.161 8.5235 6.3325C8.7755 6.4425 9.0475 6.4995 9.3225 6.4995H11.5005C11.7765 6.4995 12.0005 6.2755 12.0005 5.9995C12.0005 5.7235 11.7765 5.4995 11.5005 5.4995H9.116C8.913 5.4025 8.519 5.2255 8.1315 5.11C8.8155 4.4195 9.167 3.3995 8.9235 2.3085C8.675 1.1965 7.77 0.303999 6.655 0.0684986C4.7125 -0.342001 3.001 1.129 3.001 2.9995C3.001 3.823 3.3335 4.5685 3.8705 5.111C3.4815 5.2265 3.088 5.403 2.8855 5.4995H0.5C0.224 5.4995 0 5.7235 0 5.9995C0 6.2755 0.224 6.4995 0.5 6.4995H2.6785C2.9555 6.4995 3.2285 6.441 3.4825 6.3305C3.854 6.169 4.3075 5.9995 4.5 5.9995C4.6855 5.9995 4.8635 6.0685 5.0005 6.1935L5.2735 6.442L4.239 7.396C3.958 7.677 3.918 8.1085 4.1445 8.4235C4.2805 8.6125 4.4915 8.7315 4.7225 8.7495C4.7435 8.751 4.7645 8.752 4.786 8.752C4.9945 8.752 5.193 8.6705 5.3295 8.5335L6.1315 7.787L8.1445 9.5815L6.586 10.798C6.2525 11.0585 5.7465 11.058 5.413 10.798L3.516 9.3175C3.254 9.1125 2.926 9 2.593 9H0.5C0.224 9 0 9.224 0 9.5C0 9.776 0.224 10 0.5 10H2.5935C2.7045 10 2.8135 10.0375 2.901 10.1055L4.798 11.5865C5.14 11.853 5.5665 12 5.9995 12C6.4325 12 6.8595 11.8535 7.201 11.5865L9.098 10.106C9.1855 10.038 9.295 10.0005 9.4055 10.0005H11.499C11.775 10.0005 11.999 9.7765 11.999 9.5005C11.999 9.2245 11.775 9.0005 11.499 9.0005L11.5 9ZM4.4995 4.4835C4.2905 4.2315 4.468 3.8505 4.7955 3.8505C4.909 3.8505 5.0505 3.904 5.1275 3.9875C5.1915 4.057 5.2835 4.1005 5.385 4.1005H6.552C6.691 4.1005 6.818 4.007 6.845 3.8705C6.8765 3.7115 6.772 3.563 6.6195 3.532L5.224 3.2525C4.668 3.141 4.28 2.612 4.3615 2.033C4.4375 1.493 4.9155 1.1 5.461 1.1H5.601V0.899999C5.601 0.678999 5.78 0.499999 6.001 0.499999C6.222 0.499999 6.401 0.678999 6.401 0.899999V1.1H6.6035C6.959 1.1 7.2775 1.262 7.4885 1.5165C7.6975 1.7685 7.52 2.1495 7.1925 2.1495C7.079 2.1495 6.9375 2.096 6.8605 2.0125C6.7965 1.943 6.7045 1.8995 6.603 1.8995H5.4495C5.3105 1.8995 5.1835 1.9925 5.156 2.1285C5.124 2.2875 5.229 2.437 5.3805 2.4675L6.7765 2.747C7.3325 2.858 7.721 3.388 7.639 3.9665C7.5625 4.5065 7.085 4.899 6.5395 4.899H6.3995V5.099C6.3995 5.32 6.2205 5.499 5.9995 5.499C5.7785 5.499 5.5995 5.32 5.5995 5.099V4.899H5.384C5.0285 4.899 4.71 4.7365 4.499 4.4825L4.4995 4.4835Z" fill="#000080"></path>
                                                            </g>
                                                            <defs>
                                                            <clipPath id="clip0_125_80">
                                                            <rect width="12" height="12" fill="white"></rect>
                                                            </clipPath>
                                                            </defs>
                                                            </svg>${tradesperson.rate_charged}`;
                                                        
                            const profileRatings = document.createElement('div');
                            profileRatings.classList.add('profileRatings');
                            profileRatings.innerHTML = `<svg width="12" height="12" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">
                                                            <g clip-path="url(#clip0_125_83)">
                                                            <path d="M0.663596 6.19998L2.4436 7.49998L1.7676 9.59348C1.65835 9.91817 1.65697 10.2695 1.76365 10.595C1.87033 10.9206 2.07937 11.2029 2.3596 11.4C2.63502 11.6034 2.96879 11.7123 3.31117 11.7106C3.65355 11.7089 3.98622 11.5966 4.2596 11.3905L6.0001 10.1095L7.7411 11.389C8.01602 11.5912 8.34799 11.701 8.68928 11.7027C9.03057 11.7044 9.3636 11.5978 9.64048 11.3982C9.91736 11.1987 10.1238 10.9165 10.2302 10.5922C10.3366 10.2679 10.3375 9.91826 10.2326 9.59348L9.5566 7.49998L11.3366 6.19998C11.6112 5.99923 11.8153 5.71685 11.9198 5.39317C12.0243 5.06949 12.0238 4.72107 11.9184 4.39767C11.8131 4.07427 11.6082 3.79244 11.3331 3.59243C11.058 3.39242 10.7267 3.28446 10.3866 3.28398H8.2001L7.5366 1.21598C7.43226 0.890456 7.22723 0.606484 6.95108 0.40501C6.67493 0.203535 6.34193 0.0949707 6.0001 0.0949707C5.65826 0.0949707 5.32526 0.203535 5.04911 0.40501C4.77296 0.606484 4.56794 0.890456 4.4636 1.21598L3.8001 3.28398H1.6156C1.27547 3.28446 0.944192 3.39242 0.669086 3.59243C0.39398 3.79244 0.189117 4.07427 0.0837571 4.39767C-0.0216025 4.72107 -0.0220688 5.06949 0.0824248 5.39317C0.186918 5.71685 0.391027 5.99923 0.665596 6.19998H0.663596Z" fill="#000080"></path>
                                                            </g>
                                                            <defs>
                                                            <clipPath id="clip0_125_83">
                                                            <rect width="12" height="12" fill="white"></rect>
                                                            </clipPath>
                                                            </defs>
                                                            </svg>${tradesperson.ratings}`;

                            profileINFO.appendChild(profileName);
                            profileINFO.appendChild(profileTradeType);
                            profileINFO.appendChild(profileTags);
                            profileINFO.appendChild(profileLocation);
                            profileINFO.appendChild(profileRate);
                            profileINFO.appendChild(profileRatings);

                            const profileBOOK = document.createElement('div');
                            profileBOOK.classList.add('cardSections', 'ProfileJOB');
                            const profileBOOKimg = document.createElement('img');
                            profileBOOKimg.src = tradesperson.profile_image;
                            profileBOOKimg.alt = 'Previous Work Image';
                            profileBOOK.appendChild(profileBOOKimg);

                            cardFisrtSection.appendChild(profileIMG);
                            cardFisrtSection.appendChild(profileINFO);
                            cardFisrtSection.appendChild(profileBOOK);

                            // card availabilty and book btn section
                            const cardSecondSection = document.createElement('div');
                            cardSecondSection.classList.add('cardSections', 'profileBOOK');
                            const cardSecondSectionSpan = document.createElement('span');
                            cardSecondSectionSpan.classList.add('availability');
                            if (tradesperson.availability) {
                                cardSecondSectionSpan.textContent = `${tradesperson.availability}`;
                            } else {
                                cardSecondSectionSpan.textContent = `Available Now`;
                            }
                            const cardSecondSectionBtn = document.createElement('button');
                            cardSecondSectionBtn.classList.add('bookBtn');
                            cardSecondSectionBtn.setAttribute('type', 'button');
                            cardSecondSectionBtn.textContent = 'Book';
                            cardSecondSectionBtn.dataset.tradespersonContact = tradesperson.contact_number;
                            cardSecondSectionBtn.dataset.tradespersonId = tradesperson.id;

                            cardSecondSection.appendChild(cardSecondSectionSpan);
                            cardSecondSection.appendChild(cardSecondSectionBtn);

                            card.appendChild(cardFisrtSection);
                            card.appendChild(cardSecondSection);


                            return card



                        }
                        console.log(data);

                        data.forEach(tradesperson => {
                            const createdCard =createCard(tradesperson);
                            tradespeopleCards.appendChild(createdCard);
                        });
                    });

                } else if (entry.target.id === "containerHolder2") {
                    alert("Job Postings section is in view");

                    const jobCardsContainer = document.querySelector('.cardJob');
                    jobCardsContainer.innerHTML = "";

                    getData('http://localhost:8000/api/v1/job-posts/').then(data => {
                        console.log(data);
                        function createJobCard(job) {
                            const card = document.createElement('div');
                            card.classList.add('card', 'jobCard');
                            card.dataset.jobId = job.id;

                            const neededTrades = document.createElement('h2');
                            neededTrades.classList.add('neededTrades');
                            neededTrades.innerHTML = `<svg width="10" height="12" viewBox="0 0 10 12" fill="none" xmlns="http://www.w3.org/2000/svg">
                                                        <path d="M8.95792 0.560364L6.87458 0.561266C6.30167 0.561266 5.83333 1.06896 5.83333 1.68848V4.77795C5.83375 5.25994 6.33583 5.5422 6.70042 5.26536L7.55333 4.61788H8.95833C9.53375 4.61788 10 4.11334 10 3.49067V1.68713C10 1.0649 9.53333 0.560364 8.95792 0.560364ZM9.15958 2.47212L8.29125 3.44017C7.95958 3.81125 7.40875 3.80854 7.08083 3.43341L6.76042 3.06684C6.6075 2.89189 6.60875 2.61821 6.76292 2.44507C6.9275 2.25975 7.20208 2.2611 7.365 2.44777L7.68875 2.81795L8.56042 1.84584C8.72333 1.66323 8.99375 1.66233 9.1575 1.84404C9.315 2.01853 9.31583 2.29672 9.15917 2.47257L9.15958 2.47212ZM3.125 5.97099C4.38833 5.97099 5.41667 4.85866 5.41667 3.49112C5.41667 2.12358 4.38833 1.01125 3.125 1.01125C1.86167 1.01125 0.833333 2.12358 0.833333 3.49112C0.833333 4.85866 1.86167 5.97099 3.125 5.97099ZM3.125 1.91302C3.92917 1.91302 4.58333 2.62091 4.58333 3.49112C4.58333 4.36133 3.92917 5.06922 3.125 5.06922C2.32083 5.06922 1.66667 4.36133 1.66667 3.49112C1.66667 2.62091 2.32083 1.91302 3.125 1.91302ZM6.25 10.2544V10.9307C6.25 11.1796 6.06375 11.3816 5.83333 11.3816C5.60292 11.3816 5.41667 11.1796 5.41667 10.9307V10.2544C5.41667 8.88687 4.38833 7.77453 3.125 7.77453C1.86167 7.77453 0.833333 8.88687 0.833333 10.2544V10.9307C0.833333 11.1796 0.647083 11.3816 0.416667 11.3816C0.18625 11.3816 0 11.1796 0 10.9307V10.2544C0 8.38954 1.40167 6.87276 3.125 6.87276C4.84833 6.87276 6.25 8.38954 6.25 10.2544Z" fill="#00006D"></path>
                                                        </svg>
                                                        ${job.trade_category} needed.`;

                            const jobTitle = document.createElement('div');
                            jobTitle.classList.add('jobTitle');
                            const title = document.createElement('h4');
                            title.textContent = job.title;
                            jobTitle.appendChild(title);
                            const jobDuration = document.createElement('div');
                            jobDuration.classList.add('jobDuration');
                            const duration = document.createElement('p');

                            const currentDate = new Date();
                            const expiryDate = new Date(job.expiry_date);
                            const timeDiff = expiryDate.getTime() - currentDate.getTime();
                            const daysLeft = Math.ceil(timeDiff / (1000 * 3600 * 24));

                            duration.textContent = `${daysLeft} days left`;
                            jobDuration.appendChild(duration);
                            jobTitle.appendChild(jobDuration);

                            const budgetAndLocation = document.createElement('div');
                            budgetAndLocation.classList.add('budgetAndLocation');
                            const jobBudget = document.createElement('div');
                            jobBudget.classList.add('jobBudget');
                            const budget = document.createElement('p');
                            budget.textContent = `GHC ${job.budget_range}`
                            jobBudget.appendChild(budget);
                            const jobLoaction = document.createElement('div');
                            jobLoaction.classList.add('jobLoaction');
                            jobLoaction.innerHTML = `<svg width="12" height="14" viewBox="0 0 12 14" fill="none" xmlns="http://www.w3.org/2000/svg">
                                                    <g clip-path="url(#clip0_132_357)">
                                                    <path d="M6 3.90863C5.60444 3.90863 5.21776 4.03556 4.88886 4.27337C4.55996 4.51118 4.30362 4.84919 4.15224 5.24466C4.00087 5.64012 3.96126 6.07528 4.03843 6.49511C4.1156 6.91493 4.30608 7.30056 4.58579 7.60324C4.86549 7.90592 5.22186 8.11204 5.60982 8.19555C5.99778 8.27906 6.39992 8.2362 6.76537 8.07239C7.13082 7.90858 7.44318 7.63118 7.66294 7.27528C7.8827 6.91937 8 6.50093 8 6.07288C8 5.49889 7.78929 4.9484 7.41422 4.54252C7.03914 4.13665 6.53043 3.90863 6 3.90863ZM6 7.15501C5.80222 7.15501 5.60888 7.09154 5.44443 6.97264C5.27998 6.85373 5.15181 6.68473 5.07612 6.48699C5.00043 6.28926 4.98063 6.07168 5.01922 5.86177C5.0578 5.65186 5.15304 5.45904 5.29289 5.3077C5.43275 5.15637 5.61093 5.0533 5.80491 5.01155C5.99889 4.96979 6.19996 4.99122 6.38268 5.07313C6.56541 5.15503 6.72159 5.29373 6.83147 5.47169C6.94135 5.64964 7 5.85886 7 6.07288C7 6.35988 6.89464 6.63512 6.70711 6.83806C6.51957 7.041 6.26522 7.15501 6 7.15501Z" fill="#000080"></path>
                                                    <path d="M6.00003 13.6478C5.57901 13.6502 5.16359 13.5433 4.78857 13.3362C4.41354 13.1291 4.08983 12.8278 3.84453 12.4575C1.93903 9.61314 0.972534 7.47486 0.972534 6.10164C0.972534 4.65876 1.50222 3.27498 2.44505 2.25471C3.38789 1.23444 4.66666 0.661255 6.00003 0.661255C7.33341 0.661255 8.61217 1.23444 9.55501 2.25471C10.4979 3.27498 11.0275 4.65876 11.0275 6.10164C11.0275 7.47486 10.061 9.61314 8.15553 12.4575C7.91024 12.8278 7.58652 13.1291 7.2115 13.3362C6.83648 13.5433 6.42106 13.6502 6.00003 13.6478ZM6.00003 1.8424C4.95624 1.84368 3.95554 2.29295 3.21747 3.09164C2.4794 3.89033 2.06423 4.97321 2.06303 6.10272C2.06303 7.19026 3.00953 9.20139 4.72753 11.7655C4.87338 11.9829 5.06472 12.1598 5.28589 12.2818C5.50706 12.4038 5.75179 12.4674 6.00003 12.4674C6.24828 12.4674 6.49301 12.4038 6.71418 12.2818C6.93535 12.1598 7.12669 11.9829 7.27253 11.7655C8.99053 9.20139 9.93703 7.19026 9.93703 6.10272C9.93584 4.97321 9.52067 3.89033 8.7826 3.09164C8.04453 2.29295 7.04383 1.84368 6.00003 1.8424Z" fill="#000080"></path>
                                                    </g>
                                                    <defs>
                                                    <clipPath id="clip0_132_357">
                                                    <rect width="12" height="12.9855" fill="white" transform="translate(0 0.662231)"></rect>
                                                    </clipPath>
                                                    </defs>
                                                    </svg> <p>${job.city}</p>`;
                            budgetAndLocation.appendChild(jobBudget);
                            budgetAndLocation.appendChild(jobLoaction);

                            const jobOwner = document.createElement('div');
                            jobOwner.classList.add('jobOwner');
                            const ownerName = document.createElement('p');
                            ownerName.textContent = `${job.tradesperson.first_name} ${job.tradesperson.last_name}`;
                            jobOwner.appendChild(ownerName);

                            const jobDiscription = document.createElement('div');
                            jobDiscription.classList.add('jobDiscription');
                            const discription = document.createElement('p');
                            discription.textContent = job.description;
                            jobDiscription.appendChild(discription);

                            const datePosted = document.createElement('div');
                            datePosted.classList.add('datePosted');

                            const createdCurrentDate = new Date();
                            const createdCreatedDate = new Date(job.created_at);
                            const createdTimeDiff = createdCurrentDate.getTime() - createdCreatedDate.getTime();
                            const daysAgo = Math.floor(createdTimeDiff / (1000 * 3600 * 24));

                            if (daysAgo === 0) {
                                datePosted.innerHTML = `<svg width="12" height="12" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">
                                                    <g clip-path="url(#clip0_132_430)">
                                                    <path d="M6 11.9091C2.6915 11.9091 0 9.41777 0 6.35535C0 3.29294 2.6915 0.801636 6 0.801636C9.3085 0.801636 12 3.29294 12 6.35535C12 9.41777 9.3085 11.9091 6 11.9091ZM6 1.72726C3.243 1.72726 1 3.80342 1 6.35535C1 8.90729 3.243 10.9835 6 10.9835C8.757 10.9835 11 8.90729 11 6.35535C11 3.80342 8.757 1.72726 6 1.72726ZM8.5 6.35535C8.5 6.09942 8.2765 5.89254 8 5.89254H6.5V3.5785C6.5 3.32256 6.276 3.11569 6 3.11569C5.724 3.11569 5.5 3.32256 5.5 3.5785V6.35535C5.5 6.61129 5.724 6.81816 6 6.81816H8C8.2765 6.81816 8.5 6.61129 8.5 6.35535Z" fill="#000049"></path>
                                                    </g>
                                                    <defs>
                                                    <clipPath id="clip0_132_430">
                                                    <rect width="12" height="12" fill="white" transform="translate(0 0.801636)"></rect>
                                                    </clipPath>
                                                    </defs>
                                                    </svg>
                                                    <p>Posted Today</p>
                                                    `;
                                
                            } else {
                                datePosted.innerHTML = `<svg width="12" height="12" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">
                                                    <g clip-path="url(#clip0_132_430)">
                                                    <path d="M6 11.9091C2.6915 11.9091 0 9.41777 0 6.35535C0 3.29294 2.6915 0.801636 6 0.801636C9.3085 0.801636 12 3.29294 12 6.35535C12 9.41777 9.3085 11.9091 6 11.9091ZM6 1.72726C3.243 1.72726 1 3.80342 1 6.35535C1 8.90729 3.243 10.9835 6 10.9835C8.757 10.9835 11 8.90729 11 6.35535C11 3.80342 8.757 1.72726 6 1.72726ZM8.5 6.35535C8.5 6.09942 8.2765 5.89254 8 5.89254H6.5V3.5785C6.5 3.32256 6.276 3.11569 6 3.11569C5.724 3.11569 5.5 3.32256 5.5 3.5785V6.35535C5.5 6.61129 5.724 6.81816 6 6.81816H8C8.2765 6.81816 8.5 6.61129 8.5 6.35535Z" fill="#000049"></path>
                                                    </g>
                                                    <defs>
                                                    <clipPath id="clip0_132_430">
                                                    <rect width="12" height="12" fill="white" transform="translate(0 0.801636)"></rect>
                                                    </clipPath>
                                                    </defs>
                                                    </svg>
                                                    <p>Posted ${daysAgo} days ago</p>
                                                    `;
                            };
                            const jobApply = document.createElement('div');
                            jobApply.classList.add('jobApply');
                            const applyBtn = document.createElement('button');
                            applyBtn.classList.add('applyBtn');
                            applyBtn.setAttribute('type', 'button');
                            applyBtn.textContent = 'Apply';
                            applyBtn.dataset.jobId = job.id;
                            jobApply.appendChild(applyBtn);

                            card.appendChild(neededTrades);
                            card.appendChild(jobTitle);
                            card.appendChild(budgetAndLocation);
                            card.appendChild(jobOwner);
                            card.appendChild(jobDiscription);
                            card.appendChild(datePosted);
                            card.appendChild(jobApply);

                            return card
                        };

                        data.forEach(job => {
                            const createdCard = createJobCard(job);
                            jobCardsContainer.appendChild(createdCard);
                        });
                    });
                }
            }
        })
    ;}, {
    threshold: 0.6   // 60% of the section must be visible
    });


const sections = document.querySelectorAll(".mainSections");

const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
    if (entry.isIntersecting) {
      console.log(entry.target.id + " is in the viewport");
      const id = entry.target.id;
      
      document.querySelectorAll(".navlist li").forEach(nav => nav.classList.remove("activeNav"));
      document.querySelector(`a[href="#${id}"]`).parentElement.classList.add("activeNav");


      // Do anything you want here 👇
      entry.target.classList.add("activeSection");

      // Operations for Notifications Section
      if (entry.target.classList.contains("Notifications_section")) {
        let dateHeaderTime = '';
        const notificationsContainer = document.querySelector('.notificationCats');
        notificationsContainer.innerHTML = "";
        if (notificationsContainer) {
            
            getData('http://localhost:8000/api/v1/notifications/').then(data => {
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

                            card.dataset.notificationId = notification.id; // Store notification ID for later use


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
      
      // Operations for Jobs Section
      if (entry.target.classList.contains("DiscoverSection")) {

        const containerHolders = document.querySelectorAll('.containerHolder');


        containerHolders.forEach(containerHolder => observecontainerHolders.observe(containerHolder));
        
      }
    
    }
  });
}, {
  threshold: 0.6   // 60% of the section must be visible
});

sections.forEach(section => observer.observe(section));

/* const observefindJobPostings = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting) {
            alert("find job postings section is in view");
        }
    })
;})

observefindJobPostings.observe(document.querySelector('.findJobPostings')); */


/* document.querySelector('.notificationCats').addEventListener('click', function(e) {
    const notificationId = e.target.dataset.notificationId;
    if (notificationId) {
        document.location.href = `/main/notification/${notificationId}`;
    }
});
 */

document.addEventListener('click', function(e) {
    const card = (e.target.closest('.notificationCardOld') || e.target.closest('.notificationCard'));
    if (card) {
        const notificationId = card.dataset.notificationId;
        if (notificationId) {
            document.location.href = `/main/notification/${notificationId}`;
        }
    }
});

document.addEventListener('click', function(e) {
    const card = e.target.closest('.card');
    if (card) {
        const tradespersonId = card.dataset.tradespersonId;
        if (tradespersonId) {
            document.location.href = `/main/tradesperson-view/${tradespersonId}`;
        }
    }
});

document.addEventListener('click', function(e) {
    const card = e.target.closest('.jobCard');
    if (card) {
        const jobId = card.dataset.jobId;
        if (jobId) {
            document.location.href = `/main/jobPostDetails/${jobId}`;
        }
    }
});


