// <!-- ========================================
//      JAVASCRIPT
// ======================================== -->


document.addEventListener(
    "DOMContentLoaded",
    function () {


        const analyzeButton =
            document.getElementById(
                "analyzeButton"
            );


        const analyzeText =
            document.getElementById(
                "analyzeText"
            );


        const analyzeIcon =
            document.getElementById(
                "analyzeIcon"
            );


        const jobDescription =
            document.getElementById(
                "jobDescription"
            );


        const loading =
            document.getElementById(
                "analysisLoading"
            );


        const result =
            document.getElementById(
                "analysisResult"
            );


        const errorBox =
            document.getElementById(
                "analysisError"
            );


        const errorMessage =
            document.getElementById(
                "errorMessage"
            );


        // ====================================
        // CSRF
        // ====================================

        function getCookie(name) {

            let cookieValue = null;

            if (
                document.cookie &&
                document.cookie !== ''
            ) {

                const cookies =
                    document.cookie.split(';');

                for (
                    let i = 0;
                    i < cookies.length;
                    i++
                ) {

                    const cookie =
                        cookies[i].trim();


                    if (
                        cookie.substring(
                            0,
                            name.length + 1
                        ) ===
                        (name + '=')
                    ) {

                        cookieValue =
                            decodeURIComponent(
                                cookie.substring(
                                    name.length + 1
                                )
                            );

                        break;

                    }

                }

            }

            return cookieValue;
        }


        // ====================================
        // CREATE TAGS
        // ====================================

        function renderTags(
            containerId,
            items
        ) {

            const container =
                document.getElementById(
                    containerId
                );


            container.innerHTML = "";


            if (
                !items ||
                items.length === 0
            ) {

                container.innerHTML =
                    '<span class="empty-tag">Not specified</span>';

                return;

            }


            items.forEach(
                function (item) {

                    const tag =
                        document.createElement(
                            "span"
                        );


                    tag.className =
                        "ai-tag";


                    tag.textContent =
                        item;


                    container.appendChild(
                        tag
                    );

                }
            );

        }


        // ====================================
        // INTERVIEW PREPARATION
        // ====================================

        function renderPreparation(
            items
        ) {

            const container =
                document.getElementById(
                    "interviewPreparation"
                );


            container.innerHTML = "";


            if (
                !items ||
                items.length === 0
            ) {

                container.innerHTML =
                    '<p class="empty-result">No preparation suggestions available.</p>';

                return;

            }


            items.forEach(
                function (item, index) {

                    const row =
                        document.createElement(
                            "div"
                        );


                    row.className =
                        "preparation-item";


                    row.innerHTML = `

                        <span class="preparation-number">
                            ${index + 1}
                        </span>

                        <span>
                            ${item}
                        </span>

                    `;


                    container.appendChild(
                        row
                    );

                }
            );

        }


        // ====================================
        // ANALYZE
        // ====================================

        analyzeButton.addEventListener(
            "click",
            async function () {


                const description =
                    jobDescription.textContent.trim();


                if (!description) {

                    errorMessage.textContent =
                        "This application does not have a job description.";

                    errorBox.classList.add(
                        "show"
                    );

                    return;

                }


                // Reset

                errorBox.classList.remove(
                    "show"
                );


                result.classList.remove(
                    "show"
                );


                loading.classList.add(
                    "show"
                );


                analyzeButton.disabled =
                    true;


                analyzeText.textContent =
                    "Analyzing...";


                analyzeIcon.textContent =
                    "◌";


                try {


                    const response =
                        await fetch(
                            "{% url 'ai_job_analysis' %}",
                            {

                                method: "POST",

                                headers: {

                                    "Content-Type":
                                        "application/json",

                                    "X-CSRFToken":
                                        getCookie(
                                            "csrftoken"
                                        ),

                                },


                                body:
                                    JSON.stringify({

                                        job_description:
                                            description

                                    })

                            }
                        );


                    const data =
                        await response.json();


                    if (!response.ok) {

                        throw new Error(
                            data.error ||
                            "Unable to analyze the job description."
                        );

                    }


                    // ====================================
                    // SUMMARY
                    // ====================================

                    document.getElementById(
                        "summary"
                    ).textContent =
                        data.summary || "";


                    // ====================================
                    // SKILLS
                    // ====================================

                    renderTags(
                        "requiredSkills",
                        data.required_skills
                    );


                    // ====================================
                    // TECHNOLOGIES
                    // ====================================

                    renderTags(
                        "technologies",
                        data.technologies
                    );


                    // ====================================
                    // EXPERIENCE
                    // ====================================

                    document.getElementById(
                        "requiredExperience"
                    ).textContent =
                        data.required_experience ||
                        "Not specified.";


                    // ====================================
                    // PREPARATION
                    // ====================================

                    renderPreparation(
                        data.interview_preparation
                    );


                    // ====================================
                    // SHOW RESULT
                    // ====================================

                    loading.classList.remove(
                        "show"
                    );


                    result.classList.add(
                        "show"
                    );


                }
                catch (error) {


                    loading.classList.remove(
                        "show"
                    );


                    errorMessage.textContent =
                        error.message;


                    errorBox.classList.add(
                        "show"
                    );

                }
                finally {


                    analyzeButton.disabled =
                        false;


                    analyzeText.textContent =
                        "Analyze Again";


                    analyzeIcon.textContent =
                        "✦";

                }

            }
        );

    }
);

