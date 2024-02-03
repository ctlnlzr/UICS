import { Component } from '@angular/core';
import { MainPageComponent } from "./main-page/main-page.component";
import { RouterOutlet } from '@angular/router';
import { DescriptionPageComponent } from './description-page/description-page.component';
import { HeaderComponent } from './header/header.component';

@Component({
    selector: 'app-root',
    standalone: true,
    templateUrl: './app.component.html',
    styleUrls: ['./app.component.css'],
    imports: [MainPageComponent, DescriptionPageComponent, RouterOutlet, HeaderComponent]
})

export class AppComponent {

}
