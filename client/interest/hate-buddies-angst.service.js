function hateBuddiesAngstService($resource) {
    const api = {
        buddies: $resource('/api/hateBuddiesAngst/')
    };
    return api;
}

export default hateBuddiesAngstService;
