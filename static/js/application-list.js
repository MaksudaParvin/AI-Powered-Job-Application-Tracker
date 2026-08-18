const searchInput =
    document.getElementById("applicationSearch");

const statusFilter =
    document.getElementById("statusFilter");

const categoryFilter =
    document.getElementById("categoryFilter");

const locationFilter =
    document.getElementById("locationFilter");

const sortFilter =
    document.getElementById("sortFilter");

const rows =
    document.querySelectorAll(".application-row");

const noResults =
    document.getElementById("noResults");


function filterApplications() {

    const search =
        searchInput.value.toLowerCase().trim();

    const status =
        statusFilter.value.toLowerCase();

    const location =
        locationFilter.value.toLowerCase();


    let visibleCount = 0;


    rows.forEach(row => {

        const title =
            row.dataset.title || "";

        const company =
            row.dataset.company || "";

        const rowStatus =
            row.dataset.status || "";

        const rowLocation =
            row.dataset.location || "";


        const matchesSearch =
            title.includes(search) ||
            company.includes(search);


        const matchesStatus =
            !status ||
            rowStatus === status;


        const matchesLocation =
            !location ||
            rowLocation.includes(location);


        const visible =
            matchesSearch &&
            matchesStatus &&
            matchesLocation;


        row.style.display =
            visible ? "grid" : "none";


        if (visible) {
            visibleCount++;
        }

    });


    if (noResults) {

        noResults.style.display =
            visibleCount === 0
                ? "block"
                : "none";

    }

}


if (searchInput) {
    searchInput.addEventListener(
        "input",
        filterApplications
    );
}


if (statusFilter) {
    statusFilter.addEventListener(
        "change",
        filterApplications
    );
}


if (locationFilter) {
    locationFilter.addEventListener(
        "change",
        filterApplications
    );
}