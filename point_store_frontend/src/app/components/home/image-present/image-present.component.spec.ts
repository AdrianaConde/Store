import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ImagePresentComponent } from './image-present.component';

describe('ImagePresentComponent', () => {
  let component: ImagePresentComponent;
  let fixture: ComponentFixture<ImagePresentComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ImagePresentComponent]
    });
    fixture = TestBed.createComponent(ImagePresentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
