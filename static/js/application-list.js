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


// DELETE MODAL

const deleteModal =
    document.getElementById("deleteModal");

const deleteForm =
    document.getElementById("deleteForm");

const deleteApplicationName =
    document.getElementById("deleteApplicationName");

const closeDeleteModal =
    document.getElementById("closeDeleteModal");

const cancelDelete =
    document.getElementById("cancelDelete");


const deleteButtons =
    document.querySelectorAll(".delete-action");


deleteButtons.forEach(button => {

    button.addEventListener("click", () => {

        const applicationId =
            button.dataset.id;

        const applicationTitle =
            button.dataset.title;


        deleteApplicationName.textContent =
            applicationTitle;


        deleteForm.action =
            `/applications/${applicationId}/delete/`;


        deleteModal.classList.add("show");

    });

});


function closeModal() {

    deleteModal.classList.remove("show");

}


closeDeleteModal.addEventListener(
    "click",
    closeModal
);


cancelDelete.addEventListener(
    "click",
    closeModal
);


deleteModal.addEventListener(
    "click",
    event => {

        if (
            event.target === deleteModal
        ) {

            closeModal();

        }

    }
);


document.addEventListener(
    "keydown",
    event => {

        if (event.key === "Escape") {

            closeModal();

        }

    }
);


