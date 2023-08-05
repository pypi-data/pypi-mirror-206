import * as amplitude from "@amplitude/analytics-browser";
export const initialize = () => amplitude.init("cef436f480b80001e09b06b6da3d3db5");
export const track = (eventInput, eventProperties = {}) => amplitude.track(eventInput, eventProperties);
export const incrementUserProps = (eventName) => {
    const identifyObj = new amplitude.Identify();
    identifyObj.add(eventName, 1);
    amplitude.identify(identifyObj);
};
export const setUserId = (userId) => amplitude.setUserId(userId);
