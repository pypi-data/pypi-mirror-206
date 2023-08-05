import * as React from "react";
import { theme } from "../constants/theme";
export const Textarea = React.forwardRef((props, ref) => {
    return (React.createElement(React.Fragment, null,
        React.createElement("textarea", Object.assign({ className: `textarea ${props.className || ""}`, rows: 4 }, props, { ref: ref, style: Object.assign({ backgroundColor: "inherit", border: "1px solid #ccc", borderRadius: "4px", fontFamily: "inherit", fontSize: 14, lineHeight: "17px", padding: 12, width: "100%", maxWidth: "100%", resize: 'vertical', opacity: props.disabled ? 0.5 : 1 }, props.style) })),
        React.createElement("style", null, `.textarea:focus-visible { outline: 1px solid ${theme.colors.primary}; }`)));
});
