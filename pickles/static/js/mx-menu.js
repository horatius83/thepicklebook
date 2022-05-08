import {LitElement, html} from 'https://cdn.skypack.dev/lit';

export class MxMenu extends LitElement {
    static properties = {
        links: {},
    };

    constructor() {
        super();
        this.links = [
            {'name': 'Pickles', 'link': '/pickles'},
            {'name': 'New Pickle', 'link': '/pickles/new'},
            {'name': 'New Review', 'link': 'review/new'},
            {'name': 'About', 'link': '/pickles/about'}
        ];
    }

    render() {
        return html`
            <link rel="stylesheet" href="/pickles/static/css/mini-css/3.0.1/mini-default.min.css" />
            <details>
                <summary>Menu</summary>
                <ul>
                    ${this.links.map((link) => {
                        return html`<ul><a href=${link.link}>${link.name}</a></ul>`;
                    })}
                </ul> 
            </details>
        `;
    }
}
customElements.define('mx-menu', MxMenu);