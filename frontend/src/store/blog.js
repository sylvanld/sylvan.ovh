import http from '@/plugins/http'

/**
 * Convert article title to a viable url code.
 */
function articleCodeFromTitle(title) {
    return title
        .toLowerCase()
        .replace(/[^\w\d\s-]/g, '')
        .trim()
        .replace(/\s+/g, "-");
}

/**
 * Load proper article from an object
 */
function loadArticle(articleData) {
    const article = articleData;
    article.created_at = new Date(article.created_at);
    article.updated_at = new Date(article.updated_at);
    return article;
}

export default {
    namespaced: true,

    actions: {
        getArticle(context, { code }) {
            return new Promise(resolve => {
                http.get(`/blog/articles/${code}`)
                    .then(response => resolve(response.data));
            })
        },

        getArticles() {
            return new Promise(resolve => {
                http.get('/blog/articles')
                    .then(response => resolve(response.data.map(article => loadArticle(article))));
            })
        },

        createArticle(context, { title, content }) {
            const code = articleCodeFromTitle(title);

            return new Promise(resolve => {
                http.post('/blog/articles', { code, title, content })
                    .then(response => resolve(response.data));
            })

        },

        updateArticle(context, { code, title, content }) {
            const newCode = articleCodeFromTitle(title);

            return new Promise(resolve => {
                http.put(`/blog/articles/${code}`, { code: newCode, title, content })
                    .then(() => resolve());
            })
        },

        deleteArticle(context, { code }) {
            return new Promise(resolve => {
                http.delete(`/blog/articles/${code}`)
                    .then(() => resolve());
            })
        }
    }
}
