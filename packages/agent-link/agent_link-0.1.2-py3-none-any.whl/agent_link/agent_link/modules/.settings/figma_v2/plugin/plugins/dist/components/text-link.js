import * as React from "react";
import { theme } from "../constants/theme";
export function TextLink(props) {
    return (React.createElement("a", Object.assign({ target: "_blank" }, props, { style: Object.assign({ color: "blue", textDecoration: "underline" }, props.style) })));
}
export function TooltipTextLink(props) {
    return (React.createElement(TextLink, Object.assign({}, props, { style: Object.assign({ color: theme.colors.primaryLight }, props.style) })));
}
