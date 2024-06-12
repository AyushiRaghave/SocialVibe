document.addEventListener('DOMContentLoaded', function () {
    const password1 = document.getElementById('id_password1') || document.getElementById('id_new_password1');
    const password2 = document.getElementById('id_password2') || document.getElementById('id_new_password2');

    if (!password1 || !password2) {
        console.error('Password elements not found');
        return;
    }

    function validatePassword() {
        const criteria = {
            length: password1.value.length >= 8,
            uppercase: /[A-Z]/.test(password1.value),
            lowercase: /[a-z]/.test(password1.value),
            digit: /[0-9]/.test(password1.value),
            match: password1.value === password2.value
        };

        for (const [key, value] of Object.entries(criteria)) {
            const criterionElement = document.getElementById(`criteria-${key}`);
            if (!criterionElement) {
                console.warn(`Criterion element for ${key} not found`);
                continue;
            }

            // Check for existing i or span elements for icons
            let iconElement = criterionElement.querySelector('i');
            if (!iconElement) {
                console.warn(`Icon element for ${key} not found`);
                continue;
            }

            if (value) {
                criterionElement.classList.remove('text-danger');
                criterionElement.classList.add('text-success');
                iconElement.classList.remove('fa-times');
                iconElement.classList.add('fa-check');
            } else {
                criterionElement.classList.remove('text-success');
                criterionElement.classList.add('text-danger');
                iconElement.classList.remove('fa-check');
                iconElement.classList.add('fa-times');
            }
        }
    }

    password1.addEventListener('input', validatePassword);
    password2.addEventListener('input', validatePassword);
    console.log('Event listeners attached');
});



// document.addEventListener('DOMContentLoaded', function () {
//     const password1 = document.getElementById('id_password1') || document.getElementById('id_new_password1');
//     const password2 = document.getElementById('id_password2') || document.getElementById('id_new_password2');

//     console.log('Password1 element:', password1);
//     console.log('Password2 element:', password2);

//     function validatePassword() {
//         if (!password1 || !password2) return;

//         const criteria = {
//             length: password1.value.length >= 8,
//             uppercase: /[A-Z]/.test(password1.value),
//             lowercase: /[a-z]/.test(password1.value),
//             digit: /[0-9]/.test(password1.value),
//             match: password1.value === password2.value
//         };

//         console.log('Criteria:', criteria);

//         for (const [key, value] of Object.entries(criteria)) {
//             const criterionElement = document.getElementById(`criteria-${key}`);
//             if (criterionElement) {
//                 const iconElement = criterionElement.querySelector('i');
//                 if (iconElement) {
//                     if (value) {
//                         criterionElement.classList.remove('text-danger');
//                         criterionElement.classList.add('text-success');
//                         iconElement.classList.remove('fa-times');
//                         iconElement.classList.add('fa-check');
//                     } else {
//                         criterionElement.classList.remove('text-success');
//                         criterionElement.classList.add('text-danger');
//                         iconElement.classList.remove('fa-check');
//                         iconElement.classList.add('fa-times');
//                     }
//                 }
//             }
//         }
//     }

//     if (password1 && password2) {
//         password1.addEventListener('input', validatePassword);
//         password2.addEventListener('input', validatePassword);
//         console.log('Event listeners attached');
//     } else {
//         console.log('Password elements not found');
//     }
// });
