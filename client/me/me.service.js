function meService($http) {
    const api = {
        me() {
            return $http.get('/api/me/').then(response => {

                return response.data;
            })
        }
    }; // 'interests' derived from api/urls.py

    return api;
}

export default meService;