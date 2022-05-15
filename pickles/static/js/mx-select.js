import {LitElement, html} from 'https://cdn.skypack.dev/lit';

export class MxSelect extends LitElement {
    static properties = {
        mxLabel: {type: String},
        mxName: {type: String},
        endpoint: {type: String},
        elements: {type: Array}
    };

    constructor() {
        super();
        this.mxLabel = '';
        this.mxName = '';
        this.endpoint = '';
        this.elements = [];
    }

    onLoad = async () => {
        if (this.endpoint) {
            try {
                const result = await fetch(this.endpoint, {
                    headers: {
                        'Accept': 'application/json',
                        'X-Requested-With': 'XMLHttpRequest'
                    }
                });
                this.elements = await result.json();
                this.elements.sort((a, b) => a.name.localeCompare(b.name));
            } catch (e) {
                console.error(e);
            }
        } else {
            console.error("mx-inputsearch : endpoint is not defined");
        }
    };

    connectedCallback() {
        super.connectedCallback();
        window.addEventListener('load', this.onLoad);
    }

    disconnectedCallback() {
        window.removeEventListener('load', this.onLoad);
        super.disconnectedCallback();
    }

    render() {
        return html`
            <link rel="stylesheet" href="/pickles/static/css/mini-css/3.0.1/mini-default.min.css" />
            <div class="input-group vertical">
                <label for="${this.mxName}">${this.mxLabel} </label>
                <select name="${this.mxName}" id="${this.mxName}">
                    ${this.elements.map((e) => {
                        return html`<option value=${e.id}">${e.name}</option>`
                    })}
                </select>
            </div>
        `;
    }
}
customElements.define('mx-select', MxSelect);