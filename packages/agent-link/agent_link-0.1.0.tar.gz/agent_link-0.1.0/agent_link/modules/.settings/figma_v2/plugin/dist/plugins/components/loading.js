import * as React from "react";
import { sample } from "lodash";
import "./loading.css";
import { Box, Typography } from "@material-ui/core";
const videos = [
    "https://cdn.builder.io/o/assets%2FYJIGb4i01jvw0SRdL5Bt%2F0cbf3e32f83741bbae95b338269e8c03%2Fcompressed?apiKey=YJIGb4i01jvw0SRdL5Bt&token=0cbf3e32f83741bbae95b338269e8c03&alt=media&optimized=true",
    "https://cdn.builder.io/o/assets%2FYJIGb4i01jvw0SRdL5Bt%2Fe5d14768ef714b93a8609b8e27771c06%2Fcompressed?apiKey=YJIGb4i01jvw0SRdL5Bt&token=e5d14768ef714b93a8609b8e27771c06&alt=media&optimized=true",
    "https://cdn.builder.io/o/assets%2FYJIGb4i01jvw0SRdL5Bt%2F1eb4b6ddc2aa49dbafbf27f35b8d9654%2Fcompressed?apiKey=YJIGb4i01jvw0SRdL5Bt&token=1eb4b6ddc2aa49dbafbf27f35b8d9654&alt=media&optimized=true",
    "https://cdn.builder.io/o/assets%2FYJIGb4i01jvw0SRdL5Bt%2Fcf1e057637524e479f09981f6f590c78%2Fcompressed?apiKey=YJIGb4i01jvw0SRdL5Bt&token=cf1e057637524e479f09981f6f590c78&alt=media&optimized=true",
    "https://cdn.builder.io/o/assets%2FYJIGb4i01jvw0SRdL5Bt%2F4d042732ee134e7d90a1d51b7c593859%2Fcompressed?apiKey=YJIGb4i01jvw0SRdL5Bt&token=4d042732ee134e7d90a1d51b7c593859&alt=media&optimized=true",
    "https://cdn.builder.io/o/assets%2FYJIGb4i01jvw0SRdL5Bt%2Fe20ea9e6999a4329a19bced92a604a34%2Fcompressed?apiKey=YJIGb4i01jvw0SRdL5Bt&token=e20ea9e6999a4329a19bced92a604a34&alt=media&optimized=true",
    "https://cdn.builder.io/o/assets%2FYJIGb4i01jvw0SRdL5Bt%2F0b5bff0bec3d43e1a86d003bcaf1ac81%2Fcompressed?apiKey=YJIGb4i01jvw0SRdL5Bt&token=0b5bff0bec3d43e1a86d003bcaf1ac81&alt=media&optimized=true",
    "https://cdn.builder.io/o/assets%2FYJIGb4i01jvw0SRdL5Bt%2Fc91ff409375741fb9f8b4054170dcdf6%2Fcompressed?apiKey=YJIGb4i01jvw0SRdL5Bt&token=c91ff409375741fb9f8b4054170dcdf6&alt=media&optimized=true",
];
// prefetch the videos
videos.forEach((url) => fetch(url, {
    // fetch priority is not in the TS types as it is relatively new and currently
    // supported by chrome only
    priority: "low",
}));
export function Loading(props) {
    let indexRef = React.useRef(0);
    const [contentIndex, setContentIndex] = React.useState(0);
    const [videoURL, setVideoURL] = React.useState(sample(videos));
    React.useEffect(() => {
        const interval = setInterval(() => {
            setVideoURL(sample(videos));
            if (props.content && indexRef.current < props.content.length - 1) {
                indexRef.current += 1;
                setContentIndex(indexRef.current);
            }
        }, 5000);
        return () => {
            clearInterval(interval);
        };
    }, []);
    return (React.createElement(Box, { border: 1, style: {
            padding: 15,
            backgroundColor: "#F4F8FF",
            borderRadius: 4,
            borderColor: "#F4F8FF",
            marginTop: 10,
        } },
        React.createElement("div", { style: {
                height: 75,
                width: 75,
                borderRadius: 150,
                position: "relative",
                margin: "auto",
            } },
            React.createElement("div", { className: "loader" }),
            React.createElement("video", { key: videoURL, autoPlay: true, muted: true, loop: true, playsInline: true, style: {
                    height: "100%",
                    width: "100%",
                    objectPosition: "center",
                    objectFit: "contain",
                    filter: "none !important",
                    pointerEvents: "none",
                    mixBlendMode: "darken",
                    borderRadius: 150,
                } },
                React.createElement("source", { type: "video/mp4", src: videoURL }))),
        React.createElement("div", null,
            React.createElement(Typography, { variant: "caption", style: {
                    textAlign: "center",
                    marginTop: 10,
                    color: "#1A73E8",
                    marginBottom: -10,
                    fontStyle: "italic",
                } }, props.content && (React.createElement("p", { dangerouslySetInnerHTML: {
                    __html: props.content[contentIndex].data.textContent,
                } }))))));
}
