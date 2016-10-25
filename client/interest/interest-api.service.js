function interestAPIService($resource) {
    const api = {
        interests: $resource('/api/interests/'),
    }; // 'interests' derived from api/urls.py

    return api;
}

export default interestAPIService;