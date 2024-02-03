import { DescriptionPageComponent } from './description-page/description-page.component';
import { MainPageComponent } from './main-page/main-page.component';
import { Routes } from '@angular/router';

export const routes: Routes = [
    { path: 'definition', component: DescriptionPageComponent },
    { path: 'home', component: MainPageComponent }
];
