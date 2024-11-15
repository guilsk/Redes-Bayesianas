import { Component, OnInit } from '@angular/core';
import { ApiService } from './shared/api.service';

@Component({
	selector: 'app-home',
	templateUrl: './home.component.html',
	styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {
	data: any;

	constructor(private apiService: ApiService) { }

	public ngOnInit() {
		console.log(this.postData())
	}

	public postData() {
		const dataToSend = { name: 'Test', value: 123 };
		this.apiService.postData(dataToSend).subscribe(response => {
			console.log('Resposta do post:', response);
		});
	}
}
