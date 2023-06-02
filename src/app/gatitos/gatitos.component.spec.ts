import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GatitosComponent } from './gatitos.component';

describe('GatitosComponent', () => {
  let component: GatitosComponent;
  let fixture: ComponentFixture<GatitosComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [GatitosComponent]
    });
    fixture = TestBed.createComponent(GatitosComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
