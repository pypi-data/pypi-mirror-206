import { ReglWrapper } from "./regl_wrap";
import { SingleMarkerGL, SingleMarkerGlyphView } from "./single_marker";
import { GLMarkerType } from "./types";
import { Arrayable } from "../../../core/types";
import { Corners } from "../../../core/util/bbox";
type LRTBLikeView = SingleMarkerGlyphView & {
    sleft: Arrayable<number>;
    sright: Arrayable<number>;
    stop: Arrayable<number>;
    sbottom: Arrayable<number>;
    border_radius?: Corners<number>;
};
export declare class LRTBGL extends SingleMarkerGL {
    readonly glyph: LRTBLikeView;
    constructor(regl_wrapper: ReglWrapper, glyph: LRTBLikeView);
    get marker_type(): GLMarkerType;
    protected _set_data(): void;
    protected _set_once(): void;
}
export {};
//# sourceMappingURL=lrtb.d.ts.map