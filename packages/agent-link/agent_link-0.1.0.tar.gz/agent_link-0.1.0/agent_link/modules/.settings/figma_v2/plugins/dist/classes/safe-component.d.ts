import * as React from "react";
import { IReactionOptions } from "mobx";
declare type VoidFunction = () => void;
/**
 * Provides error boundaries for safety (one component errors won't crash the whole app)
 * and adds some methods for safe handling of subscriptions and reactions (that
 * unsubscribe when the component is destroyed)
 */
export declare class SafeComponent<P extends object = {}, S = any> extends React.Component<P, S> {
    private _unMounted;
    protected unmountDestroyers: VoidFunction[];
    onDestroy(cb: VoidFunction): void;
    componentWillUnmount(): void;
    safeListenToEvent(target: EventTarget, event: string, handler: EventListener, options?: EventListenerOptions | boolean): void;
    safeReaction<T>(watchFunction: () => T, reactionFunction: (arg: T) => void, options?: IReactionOptions): void;
}
export {};
