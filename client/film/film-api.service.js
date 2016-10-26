function filmAPIService($resource) {
    const api = {
        films: $resource('api/films/'),
    };  //'films' derived from api/urls.py

    return api;
}

export default filmAPIService;