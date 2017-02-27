describe("helloTest", function() {
    it("says hello world", function() {
        expect(helloWorld()).toContain("World");
    });
});