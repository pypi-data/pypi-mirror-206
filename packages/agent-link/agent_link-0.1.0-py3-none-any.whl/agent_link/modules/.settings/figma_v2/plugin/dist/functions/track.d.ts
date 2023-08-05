import * as amplitude from "@amplitude/analytics-browser";
export declare const initialize: () => amplitude.Types.AmplitudeReturn<void>;
export declare const track: (eventInput: string, eventProperties?: any) => amplitude.Types.AmplitudeReturn<amplitude.Types.Result>;
export declare const incrementUserProps: (eventName: string) => void;
export declare const setUserId: (userId: string) => void;
