import React from 'react';
import { render, screen } from '@testing-library/react';
import CourseDetail from './CourseDetail';

test('renders CourseDetail component', () => {
    render(<CourseDetail match={{ params: { id: 1 } }} />);
    const titleElement = screen.getByText(/Course Title/i);
    expect(titleElement).toBeInTheDocument();
});
