switch (menuOption) {
    case "Home":
        console.log("Home selected");
        break;
    case "Menu":
        console.log("Menu selected");
        break;
    case "Kontak":
        console.log("Kontak selected");
        break;
    case "Settings":
        console.log("Settings selected");
        break;
    default:
        console.error("Unknown menu option");
        process.exit(1);
}
