import Tooltip from "@material-ui/core/Tooltip";
import { HelpOutline } from "@material-ui/icons";
import * as React from "react";
import { theme } from "../constants/theme";
const omit = (obj, keys) => {
    const result = {};
    for (const key in obj) {
        if (keys.indexOf(key) === -1) {
            result[key] = obj[key];
        }
    }
    return result;
};
export function HelpTooltip(props) {
    return (React.createElement(Tooltip, Object.assign({ className: "help-tooltip" }, omit(props, ["style"]), { title: React.createElement("div", { style: { fontSize: 12 } }, props.children) }),
        React.createElement(HelpOutline, { style: Object.assign({ fontSize: 14, verticalAlign: "middle", marginLeft: 3, marginTop: -1, color: theme.colors.primary }, props.style) })));
}
