import * as React from "react";
import { reaction, action } from "mobx";
/**
 * Provides error boundaries for safety (one component errors won't crash the whole app)
 * and adds some methods for safe handling of subscriptions and reactions (that
 * unsubscribe when the component is destroyed)
 */
export class SafeComponent extends React.Component {
    constructor() {
        super(...arguments);
        this._unMounted = false;
        this.unmountDestroyers = [];
    }
    onDestroy(cb) {
        if (this._unMounted) {
            // TODO: nextTick? like promise for consistency
            cb();
        }
        else {
            this.unmountDestroyers.push(cb);
        }
    }
    // For use in react components
    componentWillUnmount() {
        this._unMounted = true;
        if (super.componentWillUnmount) {
            super.componentWillUnmount();
        }
        // FIXME: devs will likely not call super on this hook as they won't know they need to
        // and that will cause subscription leaks. Better way to do with decorators perhaps?
        for (const destroyer of this.unmountDestroyers) {
            destroyer();
        }
    }
    // TODO: metadata ways of doing this
    safeListenToEvent(target, event, handler, options) {
        const actionBoundHandler = action(handler);
        target.addEventListener(event, actionBoundHandler, options);
        this.onDestroy(() => {
            target.removeEventListener(event, actionBoundHandler);
        });
    }
    // TODO: metadata way of doing this
    // @reactions(self => [])
    safeReaction(watchFunction, reactionFunction, options = {
        fireImmediately: true,
    }) {
        this.onDestroy(reaction(watchFunction, reactionFunction, options));
    }
}
