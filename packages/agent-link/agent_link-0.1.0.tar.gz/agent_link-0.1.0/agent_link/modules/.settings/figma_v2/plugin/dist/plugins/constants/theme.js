export const theme = {
    typography: {
        fontFamily: '"Inter","Roboto", "Helvetica", "Arial", sans-serif',
    },
    page: {
        tableMaxWidth: 900,
        formMaxWidth: 700,
    },
    colors: {
        primary: "rgba(26, 115, 231, 1)",
        primaryDark: "rgb(8, 108, 193)",
        primaryLight: "rgb(7, 178, 215)",
        get primaryGradient() {
            return `linear-gradient(90deg, ${this.primary} 0px, ${this.primaryLight})`;
        },
        primaryWithOpacity(opacity) {
            return this.primary.replace("1)", opacity + ")");
        },
        green: "#00e676",
        // Aliases
        get success() {
            return this.green;
        },
        get secondary() {
            return this.green;
        },
    },
    fonts: {
        base: "",
    },
    studio: {
        tabs: {},
        container: {},
        sideBar: {},
    },
    transitions: {
        easing: "cubic-bezier(.37,.01,0,.98)",
        for(...properties) {
            return properties.map((item) => `${item} 0.3s ${this.easing}`).join(", ");
        },
    },
};
