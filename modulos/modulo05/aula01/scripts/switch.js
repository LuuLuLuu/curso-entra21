// 1) Rewrite the "switch" into an "if"

let browser = prompt();

if (browser === '' || browser === null) {

} else if (browser === 'Edge') {
    alert("You've got the Edge!")
} else if ('Chrome' || 'Firefox' || 'Safari' || 'Opera') {
    alert('Okay we support these browsers too')
}