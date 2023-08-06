/// <reference types="react" />
import { ClientStorage } from "../ui";
export declare const aiApiHost: string;
export declare function AiImport(props: {
    clientStorage: ClientStorage | null;
    updateClientStorage: (clientStorage: ClientStorage) => void;
}): JSX.Element;
