import { Directive, EventEmitter, Output, ElementRef } from '@angular/core';

@Directive({
  selector: '[appStickyFloat]'
})
export class StickyFloatDirective {

  @Output() public stuck: EventEmitter<any> = new EventEmitter();
  @Output() public unstuck: EventEmitter<any> = new EventEmitter();

  private _stuckObserver? : IntersectionObserver;
  private _unstuckObserver? : IntersectionObserver;

  constructor (private _element: ElementRef){}

  public ngAfterViewInit () {    
    
    console.log(this._element.nativeElement)
    const options = {
      root: document.querySelector('#wrapper'),
      rootMargin: '0px',
      threshold: 0.8
    }

    const options2 = {
      root: document.querySelector('#scrollArea'),
      rootMargin: '0px 0px -70%',
      threshold: 0
    }

    this._stuckObserver = new IntersectionObserver(entries => {
        this.checkForIntersection(entries, this.stuck);
    }, options);
    this._stuckObserver.observe(<Element>(this._element.nativeElement));

    this._unstuckObserver = new IntersectionObserver(entries => {
      this.checkForIntersection(entries, this.unstuck);
    }, options2);
    this._unstuckObserver.observe(<Element>(this._element.nativeElement));
  }

  private checkForIntersection = (entries: Array<IntersectionObserverEntry>, emitter: EventEmitter<any>) => {
    //console.log(entries)
    entries.forEach((entry: IntersectionObserverEntry) => {
        if (this.checkIfIntersecting(entry)) {
          emitter.emit(null);
        }
    });
  }

  private checkIfIntersecting (entry: IntersectionObserverEntry) {
    return (<any>entry).isIntersecting && entry.target === this._element.nativeElement;
  }
}
