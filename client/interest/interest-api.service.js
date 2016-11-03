function interestAPIService($resource) {
    const api = {
        interests: $resource('/api/interests/'),
        createInterests: $resource('/api/createInterests/')
    }; // 'interests' derived from api/urls.py

    return api;
}

export default interestAPIService;