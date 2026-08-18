const filterForm =
    document.getElementById("filterForm");

const searchInput =
    document.getElementById("searchInput");

const filterSelects =
    document.querySelectorAll(
        "#statusFilter, #categoryFilter, #locationFilter, #sortFilter"
    );


// ========================================
// SELECT FILTERS
// ========================================

filterSelects.forEach(select => {

    select.addEventListener(
        "change",
        () => {

            filterForm.submit();

        }
    );

});


// ========================================
// SEARCH
// ========================================

searchInput.addEventListener(
    "input",
    () => {
        filterForm.submit();
    }
);

window.addEventListener(
    "load",
    () => {

        searchInput.focus();

        searchInput.setSelectionRange(
            searchInput.value.length,
            searchInput.value.length
        );

    }
);


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


