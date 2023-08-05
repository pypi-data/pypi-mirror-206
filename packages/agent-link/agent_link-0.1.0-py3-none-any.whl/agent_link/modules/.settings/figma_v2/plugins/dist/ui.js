var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
import { Button, createMuiTheme, CssBaseline, Divider, FormControlLabel, IconButton, MuiThemeProvider, Switch, TextField, Tooltip, MenuItem, withStyles, Tabs, Tab, Box, CircularProgress, } from "@material-ui/core";
import green from "@material-ui/core/colors/green";
import { HelpOutline } from "@material-ui/icons";
import * as fileType from "file-type";
import { action, computed, observable, when } from "mobx";
import { observer } from "mobx-react";
import * as pako from "pako";
import * as React from "react";
import * as ReactDOM from "react-dom";
import * as md5 from "spark-md5";
import * as traverse from "traverse";
import { arrayBufferToBase64 } from "../lib/functions/buffer-to-base64";
import { SafeComponent } from "./classes/safe-component";
import { settings } from "./constants/settings";
import { theme as themeVars } from "./constants/theme";
import { fastClone } from "./functions/fast-clone";
import { transformWebpToPNG } from "./functions/encode-images";
import { traverseLayers } from "./functions/traverse-layers";
import "./ui.css";
import { IntlProvider, FormattedMessage } from "react-intl";
import { en, ru } from "./localize/i18n";
import { Loading } from "./components/loading";
import { MobileIcon } from "./components/Icons/MobileIcon";
import { TabletIcon } from "./components/Icons/TabletIcon";
import { DesktopIcon } from "./components/Icons/DesktopIcon";
import * as amplitude from "./functions/track";
import { v4 as uuid } from "uuid";
import { AiImport } from "./components/ai-import";
import { Wand } from "./icons/wand";
import { useDev } from "./constants/use-dev";
export const apiHost = useDev ? "http://localhost:4000" : "https://builder.io";
amplitude.initialize();
const selectionToBuilder = (selection) => __awaiter(void 0, void 0, void 0, function* () {
    const useGzip = true;
    selection = fastClone(selection);
    traverse(selection).forEach(function (item) {
        if (this.key === "intArr") {
            this.delete();
        }
    });
    const res = yield fetch(`${apiHost}/api/v1/figma-to-builder`, {
        method: "POST",
        headers: {
            "content-type": "application/json",
        },
        body: JSON.stringify(useGzip
            ? {
                compressedNodes: pako.deflate(JSON.stringify(selection), {
                    to: "string",
                }),
            }
            : {
                nodes: selection,
            }),
    }).then((res) => {
        if (!res.ok) {
            console.error("Figma-to-builder request failed", res);
            amplitude.track("export error", {
                message: "Figma-to-builder request failed",
            });
            throw new Error("Figma-to-builder request failed");
        }
        return res.json();
    });
    return res.blocks;
});
const apiKey = process.env.API_KEY || null;
const clamp = (num, min, max) => Math.max(min, Math.min(max, num));
const theme = createMuiTheme({
    typography: themeVars.typography,
    palette: {
        primary: { main: themeVars.colors.primary },
        secondary: green,
    },
    overrides: {
        MuiButtonBase: {
            root: {
                boxShadow: "none !important",
            },
        },
        MuiTooltip: {
            tooltip: {
                fontSize: 13,
                backgroundColor: "rgba(45, 45, 45, 0.95)",
                padding: "7px 11px",
            },
        },
    },
    props: {
        MuiButtonBase: {
            style: {
                boxShadow: "none !important",
            },
            // The properties to apply
            disableRipple: true, // No more ripple, on the whole application 💣!
        },
    },
});
const StyledButton = withStyles({
    root: {
        fontSize: "12px",
        padding: "8px",
        height: "30px",
        minHeight: "unset",
        display: "flex",
        justifyContent: "center",
    },
})(MenuItem);
const BASE64_MARKER = ";base64,";
function convertDataURIToBinary(dataURI) {
    const base64Index = dataURI.indexOf(BASE64_MARKER) + BASE64_MARKER.length;
    const base64 = dataURI.substring(base64Index);
    const raw = window.atob(base64);
    const rawLength = raw.length;
    const array = new Uint8Array(new ArrayBuffer(rawLength));
    for (let i = 0; i < rawLength; i++) {
        array[i] = raw.charCodeAt(i);
    }
    return array;
}
export function getImageFills(layer) {
    const images = Array.isArray(layer.fills) &&
        layer.fills
            .filter((item) => item.type === "IMAGE" && item.visible !== false && item.opacity !== 0)
            .sort((a, b) => b.opacity - a.opacity);
    return images;
}
// TODO: CACHE!
// const imageCache: { [key: string]: Uint8Array | undefined } = {};
export function processImages(layer) {
    return __awaiter(this, void 0, void 0, function* () {
        const images = getImageFills(layer);
        const convertToSvg = (value) => {
            layer.type = "SVG";
            layer.svg = value;
            if (typeof layer.fills !== "symbol") {
                layer.fills = layer.fills.filter((item) => item.type !== "IMAGE");
            }
        };
        if (!images) {
            return Promise.resolve([]);
        }
        return Promise.all(images.map((image) => __awaiter(this, void 0, void 0, function* () {
            try {
                if (!image || !image.url) {
                    return;
                }
                const url = image.url;
                if (url.startsWith("data:")) {
                    const type = url.split(/[:,;]/)[1];
                    if (type.includes("svg")) {
                        const svgValue = decodeURIComponent(url.split(",")[1]);
                        convertToSvg(svgValue);
                        return Promise.resolve();
                    }
                    else {
                        if (url.includes(BASE64_MARKER)) {
                            image.intArr = convertDataURIToBinary(url);
                            delete image.url;
                        }
                        else {
                            console.info("Found data url that could not be converted", url);
                        }
                        return;
                    }
                }
                const isSvg = url.endsWith(".svg");
                // Proxy returned content through Builder so we can access cross origin for
                // pulling in photos, etc
                const res = yield fetch(`${apiHost}/api/v1/proxy-api?url=${encodeURIComponent(url)}`);
                const contentType = res.headers.get("content-type");
                if (isSvg || (contentType === null || contentType === void 0 ? void 0 : contentType.includes("svg"))) {
                    const text = yield res.text();
                    convertToSvg(text);
                }
                else {
                    const arrayBuffer = yield res.arrayBuffer();
                    const type = fileType(arrayBuffer);
                    if (type && (type.ext.includes("svg") || type.mime.includes("svg"))) {
                        convertToSvg(yield res.text());
                        return;
                    }
                    else {
                        const intArr = new Uint8Array(arrayBuffer);
                        delete image.url;
                        if (type &&
                            (type.ext.includes("webp") || type.mime.includes("image/webp"))) {
                            const pngArr = yield transformWebpToPNG(intArr);
                            image.intArr = pngArr;
                        }
                        else {
                            image.intArr = intArr;
                        }
                    }
                }
            }
            catch (err) {
                console.warn("Could not fetch image", layer, err);
            }
        })));
    });
}
function TabPanel(props) {
    const { children, value, index } = props;
    return value === index ? (React.createElement("div", { style: Object.assign({ flexGrow: 1 }, props.style), hidden: value !== index, id: `simple-tabpanel-${index}` }, value === index && children)) : null;
}
let App = class App extends SafeComponent {
    constructor() {
        super(...arguments);
        this.editorRef = null;
        this.loading = false;
        this.loadingCmsData = false;
        this.lipsum = false;
        this.loadingGenerate = false;
        this.clientStorage = null;
        this.errorMessage = "";
        this.generatingCode = false;
        this.urlValue = "https://www.builder.io";
        this.width = "1200";
        this.online = navigator.onLine;
        this.useFrames = false;
        this.showMoreOptions = true;
        this.selection = [];
        this.selectionWithImages = null;
        this.commandKeyDown = false;
        this.shiftKeyDown = false;
        this.altKeyDown = false;
        this.ctrlKeyDown = false;
        this.showRequestFailedError = false;
        this.showImportInvalidError = false;
        this.isValidImport = null;
        this.displayFiddleUrl = "";
        this.currentLanguage = "en";
        this.tabIndex = 0;
        this.figmaCheckList = {};
        this.loaderContent = [
            {
                id: "1a",
                data: {
                    type: "during",
                    textContent: "Getting everything ready... This can take a few minutes to complete.",
                },
            },
        ];
        this.editorScriptAdded = false;
        this.form = null;
        this.urlInputRef = null;
        this.iframeRef = null;
        this.initialized = false;
        this.saveUpdates = () => {
            if (this.selection.length) {
                parent.postMessage({
                    pluginMessage: {
                        type: "updateElements",
                        elements: fastClone(this.selection),
                    },
                }, "*");
            }
        };
        this.onCreate = () => {
            if (this.loading) {
                return;
            }
            if (!this.validate()) {
                if (!this.urlValid) {
                    this.errorMessage = "Please enter a valid URL";
                    return;
                }
            }
            this.loading = true;
            if (this.urlValue) {
                const width = clamp(parseInt(this.width) || 1200, 200, 3000);
                const widthString = String(width);
                this.width = widthString;
                const encocedUrl = encodeURIComponent(this.urlValue);
                // We need to run the code to process DOM through a backend to run it in a headless browser.
                // Builder.io provides this for the Figma plugin for free.
                fetch(`${apiHost}/api/v1/url-to-figma?url=${encocedUrl}&width=${width}&useFrames=${this.useFrames}`)
                    .then((res) => {
                    if (!res.ok) {
                        console.error("Url-to-figma failed", res);
                        amplitude.track("import error");
                        throw new Error("Url-to-figma failed");
                    }
                    amplitude.incrementUserProps("import_count");
                    amplitude.track("import to figma", {
                        url: this.urlValue,
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
                    parent.postMessage({ pluginMessage: { type: "import", data: data[0] } }, "*");
                })
                    .catch((err) => {
                    this.loading = false;
                    console.error(err);
                    alert(err);
                });
            }
        };
        this.onCancel = () => {
            parent.postMessage({ pluginMessage: { type: "cancel" } }, "*");
        };
        this.switchTab = (event, newValue) => {
            this.tabIndex = newValue;
        };
    }
    // TODO: THIS IS UNUSED
    getImageUrl(intArr, imageHash) {
        var _a, _b;
        return __awaiter(this, void 0, void 0, function* () {
            const hash = imageHash !== null && imageHash !== void 0 ? imageHash : md5.ArrayBuffer.hash(intArr);
            const fromCache = hash && ((_b = (_a = this.clientStorage) === null || _a === void 0 ? void 0 : _a.imageUrlsByHash) === null || _b === void 0 ? void 0 : _b[hash]);
            if (fromCache) {
                console.debug("Used URL from cache", fromCache);
                return fromCache;
            }
            if (!apiKey) {
                console.warn("Tried to upload image without API key");
                return null;
            }
            return fetch(`${apiHost}/api/v1/upload?apiKey=${apiKey}`, {
                method: "POST",
                body: JSON.stringify({
                    image: arrayBufferToBase64(intArr),
                }),
                headers: {
                    "content-type": "application/json",
                },
            })
                .then((res) => res.json())
                .then((data) => {
                const { url } = data;
                if (typeof url !== "string") {
                    return null;
                }
                if (this.clientStorage && hash) {
                    if (!this.clientStorage.imageUrlsByHash) {
                        this.clientStorage.imageUrlsByHash = {};
                    }
                    this.clientStorage.imageUrlsByHash[hash] = url;
                }
                return url;
            });
        });
    }
    getDataForSelection(name, multipleValuesResponse = null) {
        if (!this.selection.length) {
            return multipleValuesResponse;
        }
        const firstNode = this.selection[0];
        let value = firstNode.data && firstNode.data[name];
        for (const item of this.selection.slice(1)) {
            const itemValue = item.data && item.data[name];
            if (itemValue !== value) {
                return multipleValuesResponse;
            }
        }
        return value;
    }
    updateStorage() {
        return __awaiter(this, void 0, void 0, function* () {
            yield when(() => !!this.clientStorage);
            parent.postMessage({
                pluginMessage: {
                    type: "setStorage",
                    data: fastClone(this.clientStorage),
                },
            }, "*");
        });
    }
    setDataForSelection(name, value) {
        for (const node of this.selection) {
            if (!node.data) {
                node.data = {
                    [name]: value,
                };
            }
            else {
                node.data[name] = value;
            }
        }
        // TODO: throttleNextTick
        this.saveUpdates();
    }
    get urlValid() {
        function validURL(str) {
            var pattern = new RegExp("^(https?:\\/\\/)?" + // protocol
                "((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|" + // domain name
                "((\\d{1,3}\\.){3}\\d{1,3}))" + // OR ip (v4) address
                "(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*" + // port and path
                "(\\?[;&a-z\\d%_.~+=-]*)?" + // query string
                "(\\#[-a-z\\d_]*)?$", "i"); // fragment locator
            return !!pattern.test(str);
        }
        return validURL(this.urlValue);
    }
    updateKeyPositions(event) {
        this.commandKeyDown = event.metaKey;
        this.altKeyDown = event.altKey;
        this.shiftKeyDown = event.shiftKey;
        this.ctrlKeyDown = event.ctrlKey;
    }
    getCode(useFiddle = false) {
        return __awaiter(this, void 0, void 0, function* () {
            this.displayFiddleUrl = "";
            this.showImportInvalidError = false;
            this.showRequestFailedError = false;
            if (!this.lipsum) {
                this.selectionWithImages = null;
                parent.postMessage({
                    pluginMessage: {
                        type: "getSelectionWithImages",
                    },
                }, "*");
                this.generatingCode = true;
                yield when(() => !!this.selectionWithImages);
            }
            else {
                this.selectionWithImages = this.selection;
            }
            if (!(this.selectionWithImages && this.selectionWithImages[0])) {
                console.warn("No selection with images");
                return;
            }
            // TODO: analyze if page is properly nested and annotated, if not
            // suggest in the UI what needs grouping
            const selectionToBuilderPromise = selectionToBuilder(this.selectionWithImages).catch((err) => {
                this.loadingGenerate = false;
                this.generatingCode = false;
                this.showRequestFailedError = true;
                amplitude.track("export error");
                throw err;
            });
            const imagesPromises = [];
            const imageMap = {};
            for (const layer of this.selectionWithImages) {
                traverseLayers(layer, (node) => {
                    const imageFills = getImageFills(node);
                    if (Array.isArray(imageFills) && imageFills.length) {
                        imageFills.forEach((image) => {
                            var _a;
                            if ((_a = image) === null || _a === void 0 ? void 0 : _a.intArr) {
                                imagesPromises.push((() => __awaiter(this, void 0, void 0, function* () {
                                    const { id } = yield fetch(`${apiHost}/api/v1/stage-image`, {
                                        method: "POST",
                                        body: JSON.stringify({
                                            image: arrayBufferToBase64(image.intArr),
                                        }),
                                        headers: {
                                            "content-type": "application/json",
                                        },
                                    }).then((res) => {
                                        if (!res.ok) {
                                            console.error("Image upload failed", res);
                                            throw new Error("Image upload failed");
                                        }
                                        return res.json();
                                    });
                                    delete node.intArr;
                                    imageMap[node.id] = id;
                                }))());
                            }
                        });
                    }
                });
            }
            const blocks = yield selectionToBuilderPromise;
            yield Promise.all(imagesPromises).catch((err) => {
                this.loadingGenerate = false;
                this.generatingCode = false;
                this.showRequestFailedError = true;
                amplitude.track("export error");
                throw err;
            });
            traverse(blocks).forEach((item) => {
                var _a, _b, _c, _d;
                if ((item === null || item === void 0 ? void 0 : item["@type"]) === "@builder.io/sdk:Element") {
                    const image = imageMap[(_a = item.meta) === null || _a === void 0 ? void 0 : _a.figmaLayerId];
                    if (image) {
                        const url = `https://cdn.builder.io/api/v1/image/assets%2FTEMP%2F${image}`;
                        if ((_b = item.component) === null || _b === void 0 ? void 0 : _b.options) {
                            item.component.options.image = url;
                        }
                        else if ((_d = (_c = item.responsiveStyles) === null || _c === void 0 ? void 0 : _c.large) === null || _d === void 0 ? void 0 : _d.backgroundImage) {
                            item.responsiveStyles.large.backgroundImage = `url("${url}")`;
                        }
                    }
                }
            });
            const data = {
                data: {
                    blocks: blocks,
                },
            };
            this.isValidImport = null;
            parent.postMessage({
                pluginMessage: {
                    type: "checkIfCanGetCode",
                },
            }, "*");
            this.generatingCode = true;
            yield when(() => typeof this.isValidImport === "boolean");
            if (!this.isValidImport) {
                this.generatingCode = false;
                this.isValidImport = null;
                this.showImportInvalidError = true;
                amplitude.track("import error");
                return;
            }
            this.isValidImport = null;
            const json = JSON.stringify(data);
            if (useFiddle) {
                const res = yield fetch(apiHost + "/api/v1/fiddle", {
                    method: "POST",
                    headers: {
                        "content-type": "application/json",
                    },
                    body: json,
                })
                    .then((res) => {
                    if (!res.ok) {
                        console.error("Failed to create fiddle", res);
                        throw new Error("Failed to create fiddle");
                    }
                    return res.json();
                })
                    .catch((err) => {
                    this.generatingCode = false;
                    this.selectionWithImages = null;
                    this.showRequestFailedError = true;
                    amplitude.track("fiddle creation failed");
                    throw err;
                });
                if (res.url) {
                    open(res.url, "_blank");
                    this.displayFiddleUrl = res.url;
                }
                this.generatingCode = false;
                this.selectionWithImages = null;
                amplitude.incrementUserProps("export_count");
                amplitude.track("export to builder", {
                    url: this.displayFiddleUrl,
                    type: "fiddle",
                });
            }
            else {
                const blob = new Blob([json], {
                    type: "application/json",
                });
                const link = document.createElement("a");
                link.setAttribute("href", URL.createObjectURL(blob));
                link.setAttribute("download", "page.builder.json");
                document.body.appendChild(link); // Required for FF
                link.click();
                document.body.removeChild(link);
                this.generatingCode = false;
                this.selectionWithImages = null;
                amplitude.incrementUserProps("export_count");
                amplitude.track("export to builder", {
                    type: "json",
                });
            }
        });
    }
    componentDidMount() {
        window.addEventListener("message", (e) => {
            const { data: rawData } = e;
            this.initialized = true;
            const data = rawData.pluginMessage;
            if (!data) {
                return;
            }
            if (data.type === "selectionChange") {
                this.selection = data.elements;
            }
            if (data.type === "selectionWithImages") {
                this.selectionWithImages = data.elements;
            }
            if (data.type === "canGetCode") {
                this.isValidImport = data.value;
            }
            if (data.type === "doneLoading") {
                this.loading = false;
            }
            if (data.type === "storage") {
                this.clientStorage = data.data;
            }
        });
        this.loadingCmsData = true;
        fetch("https://cdn.builder.io/api/v3/content/figma-modal-items?apiKey=YJIGb4i01jvw0SRdL5Bt")
            .then((response) => {
            if (!response.ok) {
                console.error("Cannot fetch figma checklist", response);
                return;
            }
            return response.json();
        })
            .then((data) => {
            this.figmaCheckList = data;
            if (data === null || data === void 0 ? void 0 : data.results) {
                this.loaderContent = this.loaderContent.concat(data.results.filter((item) => item.data.type === "during"));
                this.loaderContent = this.loaderContent.slice().reverse();
            }
            this.loadingCmsData = false;
        });
        parent.postMessage({
            pluginMessage: {
                type: "getStorage",
            },
        }, "*");
        parent.postMessage({
            pluginMessage: {
                type: "init",
            },
        }, "*");
        // TODO: destroy on component unmount
        this.safeReaction(() => this.urlValue, () => (this.errorMessage = ""));
        this.selectAllUrlInputText();
        this.safeListenToEvent(window, "offline", () => (this.online = false));
        this.safeListenToEvent(window, "keydown", (e) => {
            this.updateKeyPositions(e);
        });
        this.safeListenToEvent(window, "keyup", (e) => {
            this.updateKeyPositions(e);
        });
        this.safeListenToEvent(window, "online", () => (this.online = true));
        this.safeReaction(() => this.clientStorage && fastClone(this.clientStorage), () => {
            if (this.clientStorage) {
                this.updateStorage();
            }
            else if (this.clientStorage === undefined) {
                this.clientStorage = { userId: uuid() };
            }
        });
        this.safeReaction(() => { var _a; return (_a = this.clientStorage) === null || _a === void 0 ? void 0 : _a.userId; }, (userId) => {
            if (userId) {
                amplitude.setUserId(userId);
                amplitude.track("figma plugin started");
            }
        });
    }
    validate() {
        if (!this.form) {
            return false;
        }
        return this.form.reportValidity();
    }
    selectAllUrlInputText() {
        const input = this.urlInputRef;
        if (input) {
            input.setSelectionRange(0, input.value.length);
        }
    }
    getLang() {
        return this.currentLanguage === "en" ? en : ru;
    }
    render() {
        var _a, _b;
        return (React.createElement(IntlProvider, { messages: this.currentLanguage === "en" ? en : ru, locale: this.currentLanguage, defaultLocale: "en" },
            React.createElement("div", { style: {
                    display: "flex",
                    flexDirection: "column",
                    overflow: "auto",
                    alignItems: "stretch",
                    height: "100%",
                } },
                React.createElement(Tabs, { variant: "fullWidth", style: {
                        minHeight: 40,
                        backgroundColor: "#F9F9F9",
                        flexShrink: 0,
                        width: settings.ui.baseWidth,
                        borderRight: "1px solid #ccc",
                    }, TabIndicatorProps: {
                        style: { transition: "none" },
                    }, value: this.tabIndex, onChange: this.switchTab, indicatorColor: "primary", textColor: "primary" },
                    React.createElement(Tab, { style: {
                            minHeight: 40,
                            minWidth: 0,
                        }, label: React.createElement("span", { style: {
                                fontSize: 12,
                                fontWeight: "bold",
                                textTransform: "none",
                            } }, "Export to Code") }),
                    React.createElement(Tab, { style: {
                            minHeight: 40,
                            minWidth: 0,
                        }, label: React.createElement("span", { style: {
                                fontSize: 12,
                                fontWeight: "bold",
                                textTransform: "none",
                            } }, "Generate with AI") }),
                    React.createElement(Tab, { style: {
                            minHeight: 40,
                            minWidth: 0,
                        }, label: React.createElement("span", { style: {
                                fontSize: 12,
                                fontWeight: "bold",
                                textTransform: "none",
                            } }, "Import from web") })),
                React.createElement(Divider, { style: { width: settings.ui.baseWidth } }),
                React.createElement(TabPanel, { style: {
                        display: "flex",
                        flexDirection: "column",
                    }, value: this.tabIndex, index: 0 },
                    React.createElement(React.Fragment, null,
                        React.createElement("div", { style: {
                                padding: 15,
                            } },
                            React.createElement("div", { style: {
                                    display: "flex",
                                    alignItems: "center",
                                    justifyContent: "space-between",
                                } },
                                React.createElement("div", { style: {
                                        display: "flex",
                                        alignItems: "center",
                                        fontWeight: "bold",
                                    } },
                                    React.createElement(FormattedMessage, { id: "title", defaultMessage: "Turn your design into code " }),
                                    React.createElement(Tooltip, { title: "Learn how to use this feature" },
                                        React.createElement("a", { style: {
                                                color: themeVars.colors.primary,
                                                marginLeft: 5,
                                                fontWeight: "bold",
                                                position: "relative",
                                            }, href: "https://www.builder.io/c/docs/import-from-figma", target: "_blank", rel: "noopenner" },
                                            React.createElement(HelpOutline, { style: { fontSize: 18 } }))))),
                            React.createElement("div", { style: {
                                    margin: "10 0 10",
                                    fontSize: 12,
                                    opacity: 0.8,
                                } },
                                React.createElement(FormattedMessage, { id: "description", defaultMessage: "Convert your Figma designs into responsive code" })),
                            this.generatingCode ? (React.createElement(React.Fragment, null,
                                " ",
                                React.createElement(Box, { style: {
                                        padding: 5,
                                        backgroundColor: "#F9F9F9",
                                        borderRadius: 4,
                                        border: "1px solid #D3D3D3",
                                        marginTop: 10,
                                    } },
                                    React.createElement("p", { style: { margin: 2, fontSize: 12, opacity: 0.8 } },
                                        React.createElement("span", { style: { fontWeight: "bold" } }, "Note: this plugin is not magic."),
                                        " ",
                                        "We attempt to import your design as best possible. You may need to make final adjustments after import, including layout, responsiveness and styling.")),
                                React.createElement(Loading, { content: this.loaderContent }))) : (React.createElement(React.Fragment, null,
                                this.figmaCheckList &&
                                    Boolean(Object.keys(this.figmaCheckList).length) ? (React.createElement("div", null,
                                    React.createElement("div", { style: {
                                            fontWeight: "bold",
                                            fontSize: 12,
                                            marginTop: 15,
                                        } },
                                        React.createElement(FormattedMessage, { id: "contentListBeforeImport", defaultMessage: "Prep your Figma file for export" })),
                                    React.createElement("ul", { style: { paddingLeft: 20, margin: 0 } }, (_a = this.figmaCheckList.results) === null || _a === void 0 ? void 0 : _a.map((item) => {
                                        if (item.data.type === "before") {
                                            return (React.createElement("li", { key: item.id },
                                                React.createElement("p", { className: "rich-text", style: {
                                                        marginTop: "auto",
                                                        marginBottom: "auto",
                                                        fontSize: 11,
                                                        opacity: 0.8,
                                                    }, dangerouslySetInnerHTML: {
                                                        __html: item.data.textContent,
                                                    } })));
                                        }
                                    })),
                                    React.createElement("div", { style: {
                                            fontWeight: "bold",
                                            marginTop: 15,
                                            fontSize: 12,
                                        } },
                                        React.createElement(FormattedMessage, { id: "contentListAfterImport", defaultMessage: "What you will need to do after import" })),
                                    React.createElement("ul", { style: { paddingLeft: 20, margin: 0 } }, (_b = this.figmaCheckList.results) === null || _b === void 0 ? void 0 : _b.map((item) => {
                                        if (item.data.type === "after") {
                                            return (React.createElement("li", { key: item.id },
                                                React.createElement("p", { className: "rich-text", style: {
                                                        marginTop: "auto",
                                                        marginBottom: "auto",
                                                        fontSize: 11,
                                                        opacity: 0.8,
                                                    }, dangerouslySetInnerHTML: {
                                                        __html: item.data.textContent,
                                                    } })));
                                        }
                                    })))) : (React.createElement("div", { style: { display: "flex" } },
                                    React.createElement(CircularProgress, { disableShrink: true, style: { margin: "10 auto" } }))),
                                this.showImportInvalidError && (React.createElement("div", null,
                                    React.createElement("div", { style: {
                                            color: "rgba(255, 20, 20, 1)",
                                            border: `1px solid rgba(255, 0, 0, 0.2)`,
                                            padding: "10px 10px 4px 10px",
                                            borderRadius: 5,
                                            marginTop: 10,
                                            backgroundColor: "rgba(255, 0, 0, 0.1)",
                                            alignItems: "center",
                                            cursor: "pointer",
                                            textDecoration: "none",
                                        } },
                                        React.createElement(FormattedMessage, { id: "importLayerHelp", defaultMessage: "To import a layer, that layer and all children must use " }),
                                        React.createElement("a", { style: {
                                                color: themeVars.colors.primary,
                                            }, href: "https://help.figma.com/hc/en-us/articles/360040451373-Create-dynamic-designs-with-Auto-layout", target: "_blank", rel: "noopenner" },
                                            React.createElement(FormattedMessage, { id: "autolayout", defaultMessage: "autolayout" })),
                                        React.createElement(FormattedMessage, { id: "importLayerHelp2", defaultMessage: " and vectors should be " }),
                                        React.createElement("a", { style: {
                                                color: themeVars.colors.primary,
                                            }, href: "https://github.com/BuilderIO/figma-html/#auto-layout-vectors", target: "_blank", rel: "noopenner" },
                                            React.createElement(FormattedMessage, { id: "rasterizeVectors", defaultMessage: "rasterized" })),
                                        React.createElement("div", { style: {
                                                display: "flex",
                                                flexDirection: "row-reverse",
                                            } },
                                            React.createElement(Button, { size: "small", style: { textTransform: "none" }, href: "https://www.builder.io/c/docs/import-from-figma", target: "_blank", color: "primary", rel: "noopenner" },
                                                React.createElement(FormattedMessage, { id: "learnMore", defaultMessage: "Learn more" })),
                                            React.createElement(Button, { size: "small", style: { opacity: 0.5, textTransform: "none" }, onClick: () => {
                                                    parent.postMessage({
                                                        pluginMessage: {
                                                            type: "clearErrors",
                                                            data: true,
                                                        },
                                                    }, "*");
                                                    this.showImportInvalidError = false;
                                                } },
                                                React.createElement(FormattedMessage, { id: "clearErrors", defaultMessage: "Clear errors" })))))),
                                this.showRequestFailedError && (React.createElement("div", null,
                                    React.createElement("div", { style: {
                                            color: "rgba(255, 20, 20, 1)",
                                            border: `1px solid rgba(255, 0, 0, 0.2)`,
                                            padding: 10,
                                            borderRadius: 5,
                                            backgroundColor: "rgba(255, 0, 0, 0.1)",
                                            alignItems: "center",
                                            cursor: "pointer",
                                            textDecoration: "none",
                                            marginTop: 10,
                                        } },
                                        React.createElement(FormattedMessage, { id: "errorMessage", defaultMessage: "Oh no, there was an error! To troubleshoot, if you are\r\n                            importing a whole page, try importing a smaller part of the\r\n                            page at a time, like one section or even one button" })),
                                    React.createElement("div", null,
                                        React.createElement(Button, { style: { textTransform: "none" }, size: "small", color: "primary", href: "https://www.builder.io/c/docs/import-from-figma#troubleshooting", target: "_blank", rel: "noopenner" },
                                            React.createElement(FormattedMessage, { id: "learnMore", defaultMessage: "Learn more" })),
                                        React.createElement(Button, { size: "small", style: { opacity: 0.5, textTransform: "none" }, onClick: () => {
                                                this.showRequestFailedError = false;
                                            } },
                                            React.createElement(FormattedMessage, { id: "clearErrors", defaultMessage: "Clear errors" }))))),
                                !Boolean(this.selection.length) && (React.createElement("div", { style: {
                                        color: themeVars.colors.primary,
                                        marginTop: 20,
                                        padding: 10,
                                        borderRadius: 5,
                                        textAlign: "center",
                                        backgroundColor: themeVars.colors.primaryWithOpacity(0.1),
                                    } }, this.getLang().selectLayerPop)),
                                Boolean(this.selection.length) && (React.createElement(Tooltip, { disableHoverListener: Boolean(this.selection.length), title: this.getLang().selectLayerPop },
                                    React.createElement("div", null,
                                        React.createElement(Button, { fullWidth: true, style: { marginTop: 20, textTransform: "none" }, variant: "contained", onClick: (e) => {
                                                this.getCode(true);
                                            }, disabled: !this.selection.length, color: "primary" },
                                            React.createElement(FormattedMessage, { id: "getCode", defaultMessage: "Get Code" }))))),
                                this.displayFiddleUrl && (React.createElement("div", { style: {
                                        margin: "10px 0 5px 0",
                                        textTransform: "none",
                                        textAlign: "center",
                                    } },
                                    React.createElement(FormattedMessage, { id: "done", defaultMessage: "Done! " }),
                                    React.createElement("a", { style: {
                                            color: themeVars.colors.primary,
                                            fontWeight: "bold",
                                            textDecoration: "none",
                                        }, rel: "noopenner", href: this.displayFiddleUrl, target: "_blank" },
                                        React.createElement(FormattedMessage, { id: "clickHere", defaultMessage: "Click here" })),
                                    React.createElement(FormattedMessage, { id: "clickHere2", defaultMessage: " to open your content in Builder.io and choose 'get code'" }))),
                                Boolean(this.selection.length) && (React.createElement(Button, { fullWidth: true, size: "small", style: {
                                        marginTop: 5,
                                        opacity: 0.5,
                                        textTransform: "none",
                                    }, onClick: (e) => {
                                        this.getCode(false);
                                    }, disabled: !this.selection.length },
                                    React.createElement(FormattedMessage, { id: "downloadJson", defaultMessage: "Download JSON" })))))),
                        React.createElement("div", { style: {
                                color: themeVars.colors.primary,
                                margin: "auto 15px 15px",
                                border: `1px solid ${themeVars.colors.primaryWithOpacity(0.2)}`,
                                fontWeight: "bold",
                                padding: 10,
                                borderRadius: 5,
                                backgroundColor: themeVars.colors.primaryWithOpacity(0.1),
                                display: "flex",
                                alignItems: "center",
                                cursor: "pointer",
                            }, role: "button", onClick: () => {
                                this.tabIndex = 1;
                            } },
                            React.createElement(Wand, { style: { marginRight: 15 } }),
                            "New!",
                            React.createElement("span", { style: {
                                    color: "inherit",
                                    marginLeft: 3,
                                } }, "Generate designs with AI")))),
                React.createElement(TabPanel, { value: this.tabIndex, index: 1 },
                    React.createElement(AiImport, { clientStorage: this.clientStorage, updateClientStorage: (clientStorage) => {
                            this.clientStorage = clientStorage;
                            this.updateStorage();
                        } })),
                React.createElement(TabPanel, { value: this.tabIndex, index: 2 },
                    React.createElement("div", { style: {
                            display: "flex",
                            flexDirection: "column",
                            position: "relative",
                            zIndex: 3,
                            maxWidth: settings.ui.baseWidth,
                            fontWeight: 400,
                            marginBottom: 10,
                            padding: 5,
                        } },
                        React.createElement("form", { ref: (ref) => (this.form = ref), 
                            // {...{ validate: 'true' }}
                            style: {
                                display: "flex",
                                flexDirection: "column",
                                marginBottom: -10,
                            }, onSubmit: (e) => {
                                e.preventDefault();
                                this.onCreate();
                            } },
                            React.createElement("div", { style: {
                                    margin: "15 10 10 10",
                                    fontWeight: "bold",
                                } },
                                React.createElement(FormattedMessage, { id: "importDesigns", defaultMessage: "Import designs from the web" })),
                            React.createElement("div", { style: {
                                    margin: "-3px 10px 13px",
                                    fontSize: 12,
                                    opacity: 0.8,
                                } },
                                React.createElement(FormattedMessage, { id: "importDescription", defaultMessage: "Convert website to figma design" })),
                            React.createElement("div", { style: {
                                    display: "flex",
                                    flexDirection: "column",
                                    margin: "0 10 10",
                                } },
                                React.createElement("div", { style: {
                                        display: "flex",
                                        position: "relative",
                                        marginTop: 5,
                                    } },
                                    React.createElement(TextField, { inputProps: {
                                            style: {
                                                fontSize: 12,
                                            },
                                        }, label: React.createElement("span", { style: {
                                                fontWeight: "bold",
                                                color: "#000000",
                                            } },
                                            React.createElement(FormattedMessage, { id: "urlToImport", defaultMessage: "Url to import" })), fullWidth: true, inputRef: (ref) => (this.urlInputRef = ref), disabled: this.loading, required: true, onKeyDown: (e) => {
                                            // Default cmd + a functionality as weird
                                            if ((e.metaKey || e.ctrlKey) && e.which === 65) {
                                                e.stopPropagation();
                                                e.preventDefault();
                                                if (e.shiftKey) {
                                                    const input = this.urlInputRef;
                                                    input.setSelectionRange(0, 0);
                                                }
                                                else {
                                                    this.selectAllUrlInputText();
                                                }
                                            }
                                        }, placeholder: "e.g. https://builder.io", type: "url", value: this.urlValue, onChange: (e) => {
                                            let value = e.target.value.trim();
                                            if (!value.match(/^https?:\/\//)) {
                                                value = "http://" + value;
                                            }
                                            this.urlValue = value;
                                        } })),
                                this.showMoreOptions && (React.createElement("div", { style: {
                                        display: "flex",
                                        alignItems: "flex-end",
                                        marginTop: 15,
                                    } },
                                    React.createElement("div", { style: { position: "relative", flexGrow: 1 } },
                                        React.createElement(TextField, { label: React.createElement("span", { style: {
                                                    fontWeight: "bold",
                                                    color: "#000000",
                                                } },
                                                React.createElement(FormattedMessage, { id: "width", defaultMessage: "Width" })), required: true, inputProps: {
                                                min: "200",
                                                max: "3000",
                                                step: "10",
                                                style: {
                                                    fontSize: 13,
                                                },
                                            }, disabled: this.loading, onKeyDown: (e) => {
                                                // Default cmd + a functionality as weird
                                                if ((e.metaKey || e.ctrlKey) && e.which === 65) {
                                                    e.stopPropagation();
                                                    e.preventDefault();
                                                    if (e.shiftKey) {
                                                        const input = this.urlInputRef;
                                                        input.setSelectionRange(0, 0);
                                                    }
                                                    else {
                                                        const input = this.urlInputRef;
                                                        input.setSelectionRange(0, input.value.length - 1);
                                                    }
                                                }
                                            }, placeholder: "1200", fullWidth: true, type: "number", value: this.width, onChange: (e) => {
                                                this.width = String(parseInt(e.target.value) || 1200);
                                            } }),
                                        React.createElement("div", { style: Object.assign({ position: "absolute", right: -4, top: 14, borderRadius: 100, display: "flex" }, (this.loading && {
                                                pointerEvents: "none",
                                                opacity: 0.5,
                                            })) },
                                            React.createElement(IconButton, { style: {
                                                    padding: 5,
                                                    background: "none",
                                                    color: this.width === "1200" ? "#000" : "#888",
                                                }, onClick: () => (this.width = "1200") },
                                                React.createElement(DesktopIcon, null)),
                                            React.createElement(IconButton, { style: {
                                                    padding: 5,
                                                    background: "none",
                                                    color: this.width === "900" ? "#000" : "#888",
                                                }, onClick: () => (this.width = "900") },
                                                React.createElement(TabletIcon, null)),
                                            React.createElement(IconButton, { style: {
                                                    padding: 5,
                                                    background: "none",
                                                    color: this.width === "400" ? "#000" : "#888",
                                                }, onClick: () => (this.width = "400") },
                                                React.createElement(MobileIcon, null)))),
                                    React.createElement(Tooltip, { PopperProps: {
                                            modifiers: { flip: { behavior: ["top"] } },
                                        }, enterDelay: 300, placement: "top", title: this.getLang().framesPop },
                                        React.createElement(FormControlLabel, { value: "Use Frames", disabled: this.loading, style: { marginLeft: 20 }, control: React.createElement(Switch, { size: "small", color: "primary", checked: this.useFrames, onChange: (e) => (this.useFrames = e.target.checked) }), label: React.createElement("span", { style: {
                                                    fontSize: 12,
                                                    position: "relative",
                                                    fontWeight: "bold",
                                                    top: -5,
                                                } },
                                                React.createElement(FormattedMessage, { id: "frames", defaultMessage: "Frames" })), labelPlacement: "top" }))))),
                            this.errorMessage && (React.createElement("div", { style: {
                                    color: "#721c24",
                                    backgroundColor: "#f8d7da",
                                    border: "1px solid #f5c6cb",
                                    borderRadius: 4,
                                    padding: ".75rem 1.25rem",
                                    marginTop: 20,
                                } }, this.errorMessage)),
                            !this.online && (React.createElement("div", { style: {
                                    color: "#721c24",
                                    backgroundColor: "#f8d7da",
                                    border: "1px solid #f5c6cb",
                                    borderRadius: 4,
                                    padding: ".75rem 1.25rem",
                                    marginTop: 20,
                                } },
                                React.createElement(FormattedMessage, { id: "needOnline", defaultMessage: "You need to be online to use this plugin" }))),
                            this.loading ? (React.createElement("div", { style: { margin: 10 } },
                                React.createElement(Box, { style: {
                                        padding: 5,
                                        backgroundColor: "#F9F9F9",
                                        borderRadius: 4,
                                        border: "1px solid #D3D3D3",
                                        marginBottom: 10,
                                    } },
                                    React.createElement("p", { style: { margin: 2, fontSize: 12, opacity: 0.8 } },
                                        React.createElement("span", { style: { fontWeight: "bold" } }, "Note: this plugin is not magic."),
                                        " ",
                                        "For best results, you may need to do some cleanup afterwards to make it production-ready.")),
                                React.createElement(Loading, { content: this.loaderContent }))) : (React.createElement(React.Fragment, null,
                                React.createElement("div", { style: { margin: "0 10 10" } },
                                    React.createElement(Button, { type: "submit", disabled: Boolean(this.errorMessage || this.loading || !this.online), style: {
                                            marginTop: 10,
                                            marginBottom: 15,
                                            textTransform: "none",
                                        }, fullWidth: true, color: "primary", variant: "contained", onClick: this.onCreate },
                                        React.createElement(FormattedMessage, { id: "import", defaultMessage: "Import" }))),
                                React.createElement(Divider, { style: {
                                        margin: "0 -5",
                                        maxWidth: settings.ui.baseWidth,
                                    } }),
                                React.createElement("div", { style: {
                                        padding: 15,
                                        margin: "5 -5 -5",
                                    } },
                                    React.createElement("div", { style: {
                                            fontWeight: "bold",
                                        } },
                                        React.createElement(FormattedMessage, { id: "chromeExtension", defaultMessage: "Chrome Extension" })),
                                    React.createElement("div", { style: {
                                            fontSize: 12,
                                        } },
                                        React.createElement("p", { style: {
                                                margin: "10 0",
                                                opacity: 0.8,
                                            } }, "Want to capture a page that you need to navigate to or is behind an auth wall? Then the Chrome Extension is for you!"),
                                        React.createElement("p", { style: { margin: "5 0" } },
                                            React.createElement("span", { style: { fontWeight: "bold" } }, "Step 1: "),
                                            "Use our",
                                            React.createElement("a", { style: {
                                                    color: themeVars.colors.primary,
                                                    cursor: "pointer",
                                                    textDecoration: "none",
                                                }, href: "https://chrome.google.com/webstore/detail/efjcmgblfpkhbjpkpopkgeomfkokpaim", target: "_blank" },
                                                React.createElement(FormattedMessage, { id: "chromeExtensionLink", defaultMessage: "chrome extension" }))),
                                        React.createElement("p", { style: { margin: "5 0" } },
                                            React.createElement("span", { style: { fontWeight: "bold" } }, "Step 2: "),
                                            "Upload the figma.json file",
                                            React.createElement("a", { onClick: () => {
                                                    const input = document.createElement("input");
                                                    input.type = "file";
                                                    document.body.appendChild(input);
                                                    input.style.visibility = "hidden";
                                                    input.click();
                                                    const onFocus = () => {
                                                        setTimeout(() => {
                                                            if (input.parentElement &&
                                                                (!input.files || input.files.length === 0)) {
                                                                done();
                                                            }
                                                        }, 200);
                                                    };
                                                    const done = () => {
                                                        input.remove();
                                                        this.loading = false;
                                                        window.removeEventListener("focus", onFocus);
                                                    };
                                                    window.addEventListener("focus", onFocus);
                                                    // TODO: parse and upload images!
                                                    input.addEventListener("change", (event) => {
                                                        const file = event.target
                                                            .files[0];
                                                        if (file) {
                                                            this.loading = true;
                                                            var reader = new FileReader();
                                                            // Closure to capture the file information.
                                                            reader.onload = (e) => {
                                                                const text = e.target.result;
                                                                try {
                                                                    const json = JSON.parse(text);
                                                                    Promise.all(json.layers.map((rootLayer) => __awaiter(this, void 0, void 0, function* () {
                                                                        yield traverseLayers(rootLayer, (layer) => {
                                                                            if (getImageFills(layer)) {
                                                                                return processImages(layer).catch((err) => {
                                                                                    console.warn("Could not process image", err);
                                                                                });
                                                                            }
                                                                        });
                                                                    })))
                                                                        .then(() => {
                                                                        parent.postMessage({
                                                                            pluginMessage: {
                                                                                type: "import",
                                                                                data: json,
                                                                            },
                                                                        }, "*");
                                                                        amplitude.incrementUserProps("import_count");
                                                                        amplitude.track("import to figma", {
                                                                            type: "chrome-extension",
                                                                        });
                                                                        setTimeout(() => {
                                                                            done();
                                                                        }, 1000);
                                                                    })
                                                                        .catch((err) => {
                                                                        done();
                                                                        console.error(err);
                                                                        alert(err);
                                                                    });
                                                                }
                                                                catch (err) {
                                                                    alert("File read error: " + err);
                                                                    done();
                                                                }
                                                            };
                                                            reader.readAsText(file);
                                                        }
                                                        else {
                                                            done();
                                                        }
                                                    });
                                                }, style: {
                                                    color: themeVars.colors.primary,
                                                    cursor: "pointer",
                                                } },
                                                React.createElement(FormattedMessage, { id: "uploadLink", defaultMessage: " upload here " })))))))))),
                React.createElement("div", { style: {
                        display: "flex",
                        flexDirection: "column",
                        backgroundColor: "#F9F9F9",
                        width: settings.ui.baseWidth,
                        borderRight: "1px solid #ccc",
                        marginTop: "auto",
                    } },
                    React.createElement(Divider, null),
                    useDev && (React.createElement("div", { style: {
                            color: "rgba(255, 40, 40, 1)",
                            backgroundColor: "rgba(255, 0, 0, 0.1)",
                            padding: 10,
                            borderRadius: 5,
                            whiteSpace: "pre-wrap",
                            margin: "10px 10px 0 10px",
                            textAlign: "center",
                        } },
                        "Using dev env. If you see this and you are not a developer, please",
                        " ",
                        React.createElement("a", { style: { color: "inherit" }, href: "https://github.com/BuilderIO/html-to-figma/issues", target: "_blank" }, "report it"))),
                    React.createElement("a", { style: { display: "flex" }, href: "https://www.builder.io?utm_source=figma", target: "_blank" },
                        React.createElement("img", { width: 170, height: 56, style: {
                                margin: "20px auto 10px",
                            }, src: "https://cdn.builder.io/api/v1/image/assets%2FYJIGb4i01jvw0SRdL5Bt%2F2dee283279f244c1a731330a3aa96166" })),
                    React.createElement("p", { style: {
                            fontSize: 12,
                            textAlign: "center",
                            margin: "5px auto 10px",
                            maxWidth: 240,
                        } },
                        React.createElement("a", { style: {
                                color: themeVars.colors.primary,
                                cursor: "pointer",
                                textDecoration: "none",
                            }, href: "https://www.builder.io?utm_source=figma", target: "_blank" },
                            "Builder.io",
                            " "),
                        " ",
                        React.createElement("span", { style: { opacity: 0.9 } }, "is a headless CMS that lets you drag & drop with your components.")),
                    React.createElement("div", { style: {
                            textAlign: "center",
                            display: "flex",
                            alignItems: "center",
                            fontWeight: 500,
                            fontSize: 12,
                            padding: 10,
                            gap: 10,
                            margin: "0 auto 5px",
                        } },
                        React.createElement("a", { style: {
                                color: "#000000",
                                opacity: 0.7,
                                textDecoration: "none",
                            }, href: "https://github.com/BuilderIO/html-to-figma/issues", target: "_blank" },
                            React.createElement(FormattedMessage, { id: "feedbackFooter", defaultMessage: "Feedback" })),
                        React.createElement("a", { style: {
                                color: "#000000",
                                opacity: 0.7,
                                textDecoration: "none",
                                marginLeft: 5,
                            }, href: "https://github.com/BuilderIO/html-to-figma", target: "_blank" },
                            React.createElement(FormattedMessage, { id: "source", defaultMessage: "Source" })),
                        React.createElement("a", { style: {
                                color: "#000000",
                                opacity: 0.7,
                                textDecoration: "none",
                                marginLeft: 5,
                            }, href: "https://github.com/BuilderIO/html-to-figma", target: "_blank" },
                            React.createElement(FormattedMessage, { id: "help", defaultMessage: "Help" })))))));
    }
};
__decorate([
    observable
], App.prototype, "loading", void 0);
__decorate([
    observable
], App.prototype, "loadingCmsData", void 0);
__decorate([
    observable
], App.prototype, "lipsum", void 0);
__decorate([
    observable
], App.prototype, "loadingGenerate", void 0);
__decorate([
    observable
], App.prototype, "clientStorage", void 0);
__decorate([
    observable
], App.prototype, "errorMessage", void 0);
__decorate([
    observable
], App.prototype, "generatingCode", void 0);
__decorate([
    observable
], App.prototype, "urlValue", void 0);
__decorate([
    observable
], App.prototype, "width", void 0);
__decorate([
    observable
], App.prototype, "online", void 0);
__decorate([
    observable
], App.prototype, "useFrames", void 0);
__decorate([
    observable
], App.prototype, "showMoreOptions", void 0);
__decorate([
    observable
], App.prototype, "selection", void 0);
__decorate([
    observable.ref
], App.prototype, "selectionWithImages", void 0);
__decorate([
    observable
], App.prototype, "commandKeyDown", void 0);
__decorate([
    observable
], App.prototype, "shiftKeyDown", void 0);
__decorate([
    observable
], App.prototype, "altKeyDown", void 0);
__decorate([
    observable
], App.prototype, "ctrlKeyDown", void 0);
__decorate([
    observable
], App.prototype, "showRequestFailedError", void 0);
__decorate([
    observable
], App.prototype, "showImportInvalidError", void 0);
__decorate([
    observable
], App.prototype, "isValidImport", void 0);
__decorate([
    observable.ref
], App.prototype, "previewData", void 0);
__decorate([
    observable
], App.prototype, "displayFiddleUrl", void 0);
__decorate([
    observable
], App.prototype, "currentLanguage", void 0);
__decorate([
    observable
], App.prototype, "tabIndex", void 0);
__decorate([
    observable
], App.prototype, "figmaCheckList", void 0);
__decorate([
    observable
], App.prototype, "loaderContent", void 0);
__decorate([
    computed
], App.prototype, "urlValid", null);
__decorate([
    action
], App.prototype, "updateKeyPositions", null);
__decorate([
    action
], App.prototype, "getCode", null);
__decorate([
    observable
], App.prototype, "initialized", void 0);
App = __decorate([
    observer
], App);
ReactDOM.render(React.createElement(MuiThemeProvider, { theme: theme },
    React.createElement(React.Fragment, null,
        React.createElement(CssBaseline, null),
        React.createElement(App, null))), document.getElementById("react-page"));
