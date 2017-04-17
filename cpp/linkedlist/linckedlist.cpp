/* 
 * 单链表 
 * 支持操作 
 * 插入  在链表头插入一个节点
 * 删除  在链表头删除一个节点
 * 打印  打印链表数据
 * 搜索  在链表中搜索给定值
 * 删除给定值 删除链表中给定值的节点
 * 删除链表 删除整个链表
 * */

#include<iostream>
#include<string>

using namespace std;

struct node{
    int value;
    node* next;
};

/* 
 * 创建一个空链表
 * */
node* createLink(){
    node* np = new node;
    np->next = NULL;
    return np;
}

/* 
 * 插入一个节点到链表头
 *  */
void insertNode(node* link, int value){
    node* temp = new node;
    temp->value = value;
    temp->next = link->next;
    link->next = temp;
}

/* 
 * 删除表头的节点
 *  */
void deleteNode(node* link){
    node* temp = link->next;
    link->next = temp->next;
    delete temp;
}

/* 
 * 查找满足给定值节点的前驱元素
 *  */
node* findPreNode(node* link, int value){
    node* p = link;
    while(p->next != NULL){
        if(p->next->value == value){
            break;
        } else {
            p = p->next;
        }
    }
    return p;
}

/* 
 * 寻找满足给定值的节点指针，NULL表示没有找到
 *  */
node* findByValue(node* link, int value){
    node* prenode = findPreNode(link, value);
    return prenode->next;
}

/* 
 * 删除符合指定指定的节点
 *  */
bool deleteByValue(node* link, int value){
    node* prenode = findPreNode(link, value);
    if(prenode->next == NULL){
        return false;
    } else {
        node* temp = prenode->next;
        prenode->next = temp->next;
        delete temp;
        return true;
    }
}


/* 
 * 销毁整个链表
 * */
void destroyLink(node* link){
    node* p = link;
    while(p != NULL){
        node* temp = p;
        p = p->next;
        delete  temp;
    }
}

/* 
 * 遍历输出链表数据
 *  */
void walkthrough(node* link){
    node* p = link->next;
    while(p != NULL){
        cout<< p->value <<endl;
        p = p->next;
    }
}

int main(int argc, char**argv){
    node* link = createLink();
    insertNode(link, 5);
    insertNode(link, 6);
    insertNode(link, 3);
    destroyLink(link);
}

