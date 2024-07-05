describe('Course Detail Page', () => {
    it('should load the course detail page', () => {
        cy.visit('/courses/1');
        cy.contains('Course Title');
    });
});
