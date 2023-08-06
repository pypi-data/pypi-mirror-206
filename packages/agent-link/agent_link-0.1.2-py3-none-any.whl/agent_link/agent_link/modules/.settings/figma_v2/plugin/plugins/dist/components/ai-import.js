var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
import * as React from "react";
import { Textarea } from "./textarea";
import { Button, CircularProgress } from "@material-ui/core";
import { Input } from "./input";
import { apiHost, getImageFills, processImages } from "../ui";
import { settings } from "../constants/settings";
import { traverseLayers } from "../functions/traverse-layers";
import * as amplitude from "../functions/track";
import { theme } from "../constants/theme";
import { HelpTooltip } from "./help-tooltip";
import { TextLink, TooltipTextLink } from "./text-link";
import { useDev } from "../constants/use-dev";
import { HelpOutline } from "@material-ui/icons";
export const aiApiHost = useDev
    ? "http://localhost:4000"
    : // Need to use raw function URL to support streaming
        "https://ai-to-figma-tk43uighdq-uc.a.run.app";
const numPreviews = 4;
const tryJsonParse = (str) => {
    try {
        return JSON.parse(str);
    }
    catch (err) {
        return null;
    }
};
function defaultPreviews() {
    return Array.from({ length: numPreviews }, () => "");
}
function countInstancesOf(string, char) {
    return string.split(char).length;
}
function addImagesToHtml(html, index, images) {
    let i = 0;
    return html.replace(/image\.jpg/g, () => {
        const useIndex = index + i++;
        return images[useIndex % 4] || defaultImage;
    });
}
const defaultImage = "https://cdn.builder.io/api/v1/image/assets%2FYJIGb4i01jvw0SRdL5Bt%2F72c80f114dc149019051b6852a9e3b7a";
function defaultImages() {
    return Array.from({ length: numPreviews }, () => defaultImage);
}
export function AiImport(props) {
    var _a;
    const abortControllerRef = React.useRef(null);
    const [previews, setPreviews] = React.useState(defaultPreviews());
    const images = React.useRef(defaultImages());
    const [prompt, setPrompt] = React.useState("a homepage hero");
    const [style, setStyle] = React.useState("everlane.com");
    const [openAiKey, setOpenAiKey] = React.useState((_a = props.clientStorage) === null || _a === void 0 ? void 0 : _a.openAiKey);
    const [error, setError] = React.useState(null);
    const [loading, setLoading] = React.useState(false);
    React.useEffect(() => {
        if (props.clientStorage) {
            props.updateClientStorage(Object.assign(Object.assign({}, props.clientStorage), { openAiKey }));
        }
    }, [openAiKey]);
    React.useEffect(() => {
        function handler(e) {
            const { data: rawData, source } = e;
            const data = rawData.pluginMessage;
            if (data.type === "doneLoading") {
                setLoading(false);
            }
        }
        window.addEventListener("message", handler);
        return () => window.removeEventListener("message", handler);
    }, []);
    function hasPreviews() {
        return previews.filter(Boolean).length > 0;
    }
    React.useEffect(() => {
        if (hasPreviews()) {
            parent.postMessage({
                pluginMessage: {
                    type: "resize",
                    width: 1025,
                    height: settings.ui.baseHeight,
                },
            }, "*");
        }
        else {
            parent.postMessage({
                pluginMessage: {
                    type: "resize",
                    width: settings.ui.baseWidth,
                    height: settings.ui.baseHeight,
                },
            }, "*");
        }
        return () => {
            parent.postMessage({
                pluginMessage: {
                    type: "resize",
                    width: settings.ui.baseWidth,
                    height: settings.ui.baseHeight,
                },
            }, "*");
        };
    }, [hasPreviews()]);
    function fetchImages() {
        var _a;
        return __awaiter(this, void 0, void 0, function* () {
            images.current = defaultImages();
            const response = yield fetch(`${aiApiHost}/api/v1/ai-to-figma/generate-image`, {
                method: "POST",
                signal: (_a = abortControllerRef.current) === null || _a === void 0 ? void 0 : _a.signal,
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    prompt: `A lifestyle image like would be on ${style}'s homepage. It should look like a photo taken by a photographer.`,
                    key: openAiKey,
                    size: "256x256",
                    number: numPreviews,
                }),
            });
            const json = yield response.json();
            images.current = json.images.map((img) => img.url);
            setPreviews((previews) => previews.map((preview, index) => addImagesToHtml(preview, index, images.current)));
        });
    }
    function onSubmit(e) {
        return __awaiter(this, void 0, void 0, function* () {
            e.preventDefault();
            setError(null);
            setLoading("Generating...");
            if (abortControllerRef.current) {
                abortControllerRef.current.abort();
            }
            abortControllerRef.current = new AbortController();
            setPreviews(defaultPreviews());
            fetchImages();
            try {
                const response = yield fetch(`${aiApiHost}/api/v1/ai-to-figma/preview`, {
                    method: "POST",
                    signal: abortControllerRef.current.signal,
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({
                        style: style,
                        prompt: prompt,
                        key: openAiKey,
                        number: numPreviews,
                    }),
                });
                const reader = response.body.getReader();
                const decoder = new TextDecoder("utf-8");
                const html = ["", "", "", ""];
                let fullResponseText = "";
                while (true) {
                    const { value, done } = yield reader.read();
                    if (done) {
                        break;
                    }
                    const textArr = decoder.decode(value, { stream: true }).split("\n");
                    for (const text of textArr) {
                        fullResponseText += text;
                        if (text.startsWith("data:")) {
                            try {
                                const { index, content } = JSON.parse(text.replace("data:", ""));
                                html[index] += content;
                                const item = html[index];
                                // Make sure we don't stream in partial tags like `<div ...` before we close it
                                if (countInstancesOf(item, "<") === countInstancesOf(item, ">")) {
                                    previews[index] = addImagesToHtml(item, index, images.current);
                                    setPreviews([...previews]);
                                }
                            }
                            catch (err) {
                                console.warn(`Could not parse JSON from chunk: ${text}`);
                                // Continue
                            }
                        }
                    }
                }
                const resJson = tryJsonParse(fullResponseText);
                if (resJson && resJson.error) {
                    const message = resJson.error.message;
                    setError(message);
                }
                else if (!hasPreviews() && fullResponseText.trim().length) {
                    setError(fullResponseText);
                }
            }
            catch (err) {
                console.error("Error fetching previews: ", err);
                setError(`
        We had an issue generating results. Please make sure you have a working internet connection and try again, and if this issue persists please let us know at https://github.com/BuilderIO/figma-html/issues
      `.trim());
            }
            finally {
                setLoading(false);
            }
        });
    }
    return (React.createElement("div", { style: { display: "flex" } },
        React.createElement("div", { style: {
                width: settings.ui.baseWidth,
                flexShrink: 0,
                display: "flex",
                flexDirection: "column",
                boxSizing: "border-box",
                padding: "7 20",
            } },
            React.createElement("form", { onSubmit: onSubmit },
                React.createElement("h4", null,
                    "Prompt",
                    " ",
                    React.createElement(HelpTooltip, null,
                        React.createElement(React.Fragment, null, "Be as detailed and specific as possible."))),
                React.createElement(Textarea, { onKeyPress: (e) => {
                        if (e.key === "Enter" &&
                            !(e.shiftKey || e.ctrlKey || e.altKey || e.metaKey)) {
                            onSubmit(e);
                        }
                    }, placeholder: "What do you want to create?", value: prompt, onChange: (e) => setPrompt(e.currentTarget.value), name: "prompt" }),
                React.createElement("h4", null,
                    "Style",
                    React.createElement(HelpTooltip, null,
                        React.createElement(React.Fragment, null, "Enter a well know site like 'jcrew.com'. This will guide the look and feel and be used as a basis for any images"))),
                React.createElement(Input, { placeholder: "Use a well recognized site, like 'jcrew.com'", value: style, onChange: (e) => setStyle(e.currentTarget.value), name: "style" }),
                React.createElement("h4", null,
                    "OpenAI Key",
                    React.createElement(HelpTooltip, { interactive: true },
                        React.createElement(React.Fragment, null,
                            "Please",
                            " ",
                            React.createElement(TooltipTextLink, { href: "https://platform.openai.com/signup" }, "create an account"),
                            " ",
                            "with",
                            " ",
                            React.createElement(TooltipTextLink, { href: "https://platform.openai.com/overview" }, "OpenAI"),
                            " ",
                            "and provide then grab your",
                            " ",
                            React.createElement(TooltipTextLink, { href: "https://platform.openai.com/account/api-keys" }, "API key"),
                            " ",
                            "and put it here. Be sure that you have",
                            " ",
                            React.createElement(TooltipTextLink, { href: "https://platform.openai.com/account/billing/overview" }, "billing"),
                            " ",
                            React.createElement(TooltipTextLink, { href: "https://help.openai.com/en/articles/6891831-error-code-429-you-exceeded-your-current-quota-please-check-your-plan-and-billing-details" }, "turned on"),
                            "."))),
                React.createElement(Input, { value: openAiKey, onChange: (e) => setOpenAiKey(e.currentTarget.value), type: "password", placeholder: "sk-********************", name: "key" }),
                React.createElement(Button, { disabled: !(prompt && style && openAiKey), style: { marginTop: 15 }, variant: "contained", type: "submit", fullWidth: true, color: "primary" }, "Generate"),
                React.createElement("style", null, `h4 { margin: 11px 0 7px }`)),
            error && (React.createElement("div", { style: {
                    color: "rgba(255, 40, 40, 1)",
                    marginBottom: 10,
                    backgroundColor: "rgba(255, 0, 0, 0.1)",
                    padding: 10,
                    borderRadius: 5,
                    whiteSpace: "pre-wrap",
                } }, error)),
            loading && (React.createElement("div", { style: {
                    display: "flex",
                    justifyContent: "center",
                    flexDirection: "column",
                } },
                React.createElement(CircularProgress, { style: { margin: "10 auto" }, disableShrink: true }),
                typeof loading === "string" && (React.createElement("div", { style: { margin: "10 auto" } }, loading)))),
            React.createElement(TextLink, { target: "_blank", href: "https://www.builder.io/blog/ai-figma", style: {
                    color: theme.colors.primary,
                    border: `1px solid ${theme.colors.primaryWithOpacity(0.2)}`,
                    fontWeight: "bold",
                    padding: 10,
                    borderRadius: 5,
                    backgroundColor: theme.colors.primaryWithOpacity(0.1),
                    display: "flex",
                    alignItems: "center",
                    cursor: "pointer",
                    textDecoration: "none",
                } },
                React.createElement(HelpOutline, { style: { marginRight: 10 } }),
                "Learn how to use this feature")),
        hasPreviews() && (React.createElement("div", { style: {
                backgroundColor: "#f9f9f9",
                display: "flex",
                flexWrap: "wrap",
                justifyContent: "center",
                gap: 10,
                padding: 20,
                height: 670,
                marginLeft: -1,
                borderLeft: "1px solid #ccc",
                position: "fixed",
                right: 0,
                zIndex: 5,
                top: 0,
                width: `calc(100% - ${settings.ui.baseWidth - 1}px)`,
                overflow: "auto",
            } }, previews.map((preview, index) => (React.createElement("div", { role: "button", key: index, style: {
                width: "300px",
                height: "300px",
                background: "white",
                position: "relative",
                borderRadius: "4px",
                overflow: "hidden",
                cursor: "pointer",
                border: "1px solid #ccc",
            }, onClick: () => __awaiter(this, void 0, void 0, function* () {
                var _b;
                setLoading("Importing...");
                setPreviews(defaultPreviews());
                (_b = abortControllerRef.current) === null || _b === void 0 ? void 0 : _b.abort();
                abortControllerRef.current = new AbortController();
                fetch(`${apiHost}/api/v1/url-to-figma?width=1200`, {
                    method: "POST",
                    signal: abortControllerRef.current.signal,
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({
                        html: `<div style="font-family:Arial,Helvetica,sans-serif;">${preview}</div>`,
                    }),
                })
                    .then((res) => {
                    if (!res.ok) {
                        console.error("Url-to-figma failed", res);
                        amplitude.track("import for ai error");
                        throw new Error("Url-to-figma failed");
                    }
                    amplitude.incrementUserProps("import_count");
                    amplitude.track("import to figma for ai", {
                        type: "url",
                    });
                    return res.json();
                })
                    .then((data) => {
                    const layers = data.layers;
                    return Promise.all([data].concat(layers.map((rootLayer) => __awaiter(this, void 0, void 0, function* () {
                        yield traverseLayers(rootLayer, (layer) => {
                            if (getImageFills(layer)) {
                                return processImages(layer).catch((err) => {
                                    console.warn("Could not process image", err);
                                });
                            }
                        });
                    }))));
                })
                    .then((data) => {
                    parent.postMessage({
                        pluginMessage: {
                            type: "import",
                            data: data[0],
                            blurImages: true,
                        },
                    }, "*");
                })
                    .catch((err) => {
                    console.error(err);
                    setLoading(false);
                    alert(err);
                });
            }) },
            React.createElement("div", { style: {
                    width: "300%",
                    height: "300%",
                    transform: "scale(0.3333)",
                    position: "absolute",
                    top: "0",
                    left: "0",
                    transformOrigin: "top left",
                    overflow: "auto",
                } },
                React.createElement("div", { style: {
                        pointerEvents: "none",
                    }, dangerouslySetInnerHTML: { __html: preview } })))))))));
}
