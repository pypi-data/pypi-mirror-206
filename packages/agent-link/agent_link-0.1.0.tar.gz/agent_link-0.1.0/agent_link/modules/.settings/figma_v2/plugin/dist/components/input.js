import * as React from "react";
import { theme } from "../constants/theme";
export const Input = React.forwardRef((props, ref) => {
    return (React.createElement(React.Fragment, null,
        React.createElement("input", Object.assign({ className: `input ${props.className || ""}` }, props, { ref: ref, style: Object.assign({ backgroundColor: "inherit", border: "1px solid #ccc", borderRadius: "4px", fontFamily: "inherit", fontSize: 14, lineHeight: "17px", padding: 12, width: "100%", maxWidth: "100%", opacity: props.disabled ? 0.5 : 1 }, props.style) })),
        React.createElement("style", null, `.input:focus-visible { outline: 1px solid ${theme.colors.primary}; }`)));
});
