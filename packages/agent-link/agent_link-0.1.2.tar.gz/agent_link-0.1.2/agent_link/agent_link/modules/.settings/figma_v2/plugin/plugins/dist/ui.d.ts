/// <reference types="plugin-typings" />
import "./ui.css";
export declare const apiHost: string;
export interface ClientStorage {
    imageUrlsByHash?: {
        [hash: string]: string | null;
    };
    userId?: string;
    openAiKey?: string;
}
declare type Node = TextNode | RectangleNode;
export declare function getImageFills(layer: Node): false | any[];
export declare function processImages(layer: Node): Promise<void[]>;
export {};
