#include <stdio.h>

int main() {
    char name[50];
    int units;

    printf("Enter student name: ");
    fgets(name, sizeof(name), stdin);
    printf("Enter number of registered units: ");
    scanf("%d", &units);

    printf("\n--- Final Summary ---\n");
    printf("Student Name: %s", name);
    printf("Units: %d\n", units);

    if (units > 7) {
        printf("Status: Overload – Approval Required\n");
    } else {
        printf("Status: Registration Accepted\n");
    }

    return 0;
}
