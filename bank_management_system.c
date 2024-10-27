#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_USERS 100
#define MAX_LENGTH 25

typedef struct {
    int id;
    char name[MAX_LENGTH];
    double balance;
    char password[MAX_LENGTH];
}account;

account accounts[MAX_USERS];
int user_count=0;

void Transfer_Money(){

}


void Create_Money(){
    
}


void Login(){
    
}

void Desposit(){
    
}

void Check_Amount(){
    
}

int main(){
int choice,userid;
printf("Choose desired Service:\n1.Transfer Money\n2.Create Account\n3.Login\n4.Desposit\n5.Check Amount");
scanf("%d",&choice);



}